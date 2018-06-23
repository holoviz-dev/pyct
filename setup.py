from setuptools import setup

# Temporary until build requirements as specified in pyproject.toml
# are widely supported
try:
    import pyct.build # noqa: TODO will be removed when param supplies get_setup_version2()
    import param      # noqa: see import error message below
except ImportError:
    raise ImportError("pyct requires requires param to build; please upgrade to pip>=10 and try again (or alternatively, install param manually first (e.g. `pip install param` or `conda install -c pyviz param`)")

if __name__ == "__main__":
    setup()
