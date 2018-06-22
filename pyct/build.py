import os
import shutil
import re

def examples(path, root, verbose=False, force=False):
    """
    Copies the notebooks to the supplied path.
    """
    filepath = os.path.abspath(os.path.dirname(root))
    example_dir = os.path.join(filepath, './examples')
    if not os.path.exists(example_dir):
        example_dir = os.path.join(filepath, '../examples')
    if os.path.exists(path):
        if not force:
            print('%s directory already exists, either delete it or set the force flag' % path)
            return
        shutil.rmtree(path)
    ignore = shutil.ignore_patterns('.ipynb_checkpoints', '*.pyc', '*~')
    tree_root = os.path.abspath(example_dir)
    if os.path.isdir(tree_root):
        shutil.copytree(tree_root, path, ignore=ignore, symlinks=True)
    else:
        print('Cannot find %s' % tree_root)


## temporary; should move to autover

def get_setup_version2():
    # Simpler get_setup_version() for setup.cfg files.
    # Requires [tool:autover] in setup.cfg
    from param.version import Version # undeclared dependency, but this fn should move to version anyway
    import configparser # TODO: check this works on py2 also
    import warnings
    config = configparser.ConfigParser()
    config.read("setup.cfg")
    reponame = config['tool:autover']['reponame']
    pkgname = config['tool:autover'].get('pkgname',reponame)

    ###
    # setuptools requires % to be escaped with % or it can't parse
    # setup.cfg, but then git export-subst wouldn't work :(
    # So we hack such things into section headings like
    # [tool:autover.configparser_workaround.archive_commit=$Format:%h$]
    archive_commit = None
    archive_commit_key = 'tool:autover.configparser_workaround.archive_commit'
    for section in config.sections():
        if section.startswith(archive_commit_key):
            archive_commit = re.match(".*=\s*(\S*)\s*",section).group(1)
    if archive_commit is None:
        warnings.warn("No archive commit available in setup.cfg; consequences = ...")
    ###

    # TODO: is this right? do I need the other stuff from projects' get_setup_version()?
    return Version.setup_version(os.path.dirname(os.path.abspath("setup.cfg")),reponame,pkgname=pkgname,archive_commit=archive_commit)
