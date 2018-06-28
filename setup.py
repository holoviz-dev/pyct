from setuptools import setup
####
# Build dependency checks
#
# Temporary, until pyproject.toml is widely supported. We're expecting
# most users to install a wheel or conda package, neither of which
# requires running setup.py and building a package.  So these checks
# are for packagers and those installing from e.g. github.
import setuptools
from pkg_resources import parse_version
missing_build_dep = False
if parse_version(setuptools.__version__)<parse_version('30.3.0'):
    missing_build_dep = True
try:
    import param
    if parse_version(param.__version__)<parse_version('1.6.1'):
        missing_build_dep = True
except:
    missing_build_dep = True

if missing_build_dep:
    raise ValueError('Building pyct requires setuptools>=30.3.0 and param>=1.6.1; please upgrade to pip>=10 and try again. Alternatively, install the build dependencies manually first (e.g. `pip install --upgrade "setuptools>=30.3.0" "param>=1.6.1"` or `conda install -c pyviz "setuptools>=30.3.0" "param>=1.6.1"`)')
#####

if __name__ == "__main__":
    setup()
