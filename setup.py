from setuptools import setup, find_packages
import param

NAME = 'pyct'
DESCRIPTION = 'Python package common tasks for users (e.g. copy examples, fetch data, ...)'

setup_args = dict(
    name=NAME,
    version=param.version.get_setup_version(__file__, NAME),
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
        'Programming Language :: Python :: 3.7',
        'Development Status :: 4 - Beta'
    ],
    author='PyViz',
    author_email='holoviews@gmail.com',
    maintainer='PyViz',
    maintainer_email='holoviews@gmail.com',
    url='http://{}.pyviz.org'.format(NAME),
    project_urls = {
        'Bug Tracker': 'https://github.com/pyviz/{}/issues'.format(NAME),
        'Documentation': 'https://pyviz.github.io/{}'.format(NAME),
        'Source Code': 'https://github.com/pyviz/{}'.format(NAME),
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
    }
)

if __name__ == "__main__":
    setup(**setup_args)
