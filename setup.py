from setuptools import setup, find_packages

import version

setup_args = dict(
    name = 'pyct',
    description = 'python package common tasks for users (e.g. copy examples, fetch data, ...)',
    version = version.get_setup_version('pyct'),
    license = 'BSD-3',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",    
    url = 'http://github.com/pyviz/pyct',
    packages = find_packages(),
    python_requires=">=2.7",
    include_package_data = True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',        
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],    
    install_requires=[
        'pyyaml',
        'requests'
    ],
    extras_require={'tests': ['flake8']}
)

if __name__ == "__main__":
    setup(**setup_args)
