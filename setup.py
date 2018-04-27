from setuptools import setup, find_packages

import version

setup_args = dict(
    name = 'pvutil',
    description = 'pyviz user utilities (e.g. install examples, download data, ...',
    version = version.get_setup_version('pvutil'),
    license = 'BSD-3',
    url = 'http://github.com/pyviz/pyct',
    packages = find_packages(),
    python_requires=">=2.7",
    include_package_data = True,
    install_requires=[
        'pyyaml',
        'requests'
    ],
    extras_require={'tests': ['flake8']}
)

if __name__ == "__main__":
    setup(**setup_args)
