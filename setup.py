from setuptools import setup, find_packages

# unfortunately cannot avoid duplicating this from build.py
def get_setup_version(root, reponame):
    """
    Helper to get the current version from either git describe or the
    .version file (if available) - allows for param to not be available.

    Normally used in setup.py as follows:

    >>> from pyct.build import get_setup_version
    >>> version = get_setup_version(__file__, reponame)  # noqa
    """
    import os
    import json

    filepath = os.path.abspath(os.path.dirname(root))
    version_file_path = os.path.join(filepath, reponame, '.version')
    try:
        from param import version
    except:
        version = None
    if version is not None:
        return version.Version.setup_version(filepath, reponame, archive_commit="$Format:%h$")
    else:
        print("WARNING: param>=1.6.0 unavailable. If you are installing a package, this warning can safely be ignored. If you are creating a package or otherwise operating in a git repository, you should install param>=1.6.0.")
        return json.load(open(version_file_path, 'r'))['version_string']


NAME = 'pyct'
DESCRIPTION = 'Python package common tasks for users (e.g. copy examples, fetch data, ...)'

setup_args = dict(
    name=NAME,
    version=get_setup_version(__file__, NAME),
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license='BSD 3-Clause License',
    license_file='LICENSE.txt',
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 4 - Beta'
    ],
    author='HoloViz',
    author_email='holoviews@gmail.com',
    maintainer='HoloViz',
    maintainer_email='holoviews@gmail.com',
    url='https://github.com/pyviz-dev/{}'.format(NAME),
    project_urls = {
        'Bug Tracker': 'https://github.com/pyviz-dev/{}/issues'.format(NAME),
        'Source Code': 'https://github.com/pyviz-dev/{}'.format(NAME),
    },
    include_package_data=True,
    packages=find_packages(),
    python_requires='>=2.7',
    install_requires=[
        'param >=1.7.0',
    ],
    extras_require={
        'cmd': [
            'pyyaml',
            'requests'
        ],
        'tests': [
            'flake8',
            'pytest'
        ],
        'doc': [
            'nbsite',
            'sphinx_ioam_theme'
        ],
        'build': [
            "setuptools",
            "param >=1.7.0",
        ]
    },
    entry_points = {
        'console_scripts': [
            'pyct=pyct.cmd:main',
        ],
    }
)

if __name__ == "__main__":
    setup(**setup_args)
