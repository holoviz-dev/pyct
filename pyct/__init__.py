import param
from .report import report

NAME = "pyct"

# version comes from git if available, otherwise from .version file
__version__ = str(param.version.Version(fpath=__file__, archive_commit="$Format:%h$",
                                        reponame=NAME))
