from pyctdev import *  # noqa: api


def task_pip_on_conda():
    """Experimental: provide pip build env via conda"""
    return {'actions':[
        # some ecosystem=pip build tools must be installed with conda when using conda...
        'conda install -y pip twine wheel',
        # ..and some are only available via conda-forge
        'conda install -y -c conda-forge tox "virtualenv<=20.4.7"',
    ]}
