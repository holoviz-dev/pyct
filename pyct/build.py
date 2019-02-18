import os
import shutil

def examples(root, reponame, verbose=False, force=False):
    """
    Copy example notebooks from original location to inside module
    directory.
    
    Normally used in setup.py as follows: 
    
    >>> from pyct.build import examples
    >>> examples(__file__, reponame)  # noqa
    """
    filepath = os.path.abspath(os.path.dirname(root))
    
    old_example_dir = os.path.join(filepath, 'examples')
    if not os.path.exists(old_example_dir):
        old_example_dir = os.path.join(filepath, '..', 'examples')
    if not os.path.exists(old_example_dir):
        print('No example dir found in expected location')
        return
    
    new_example_dir = os.path.join(filepath, reponame, 'examples')
    if os.path.exists(new_example_dir):
        if not force:
            print('%s directory already exists, either delete it or set the force flag' % new_example_dir)
            return
        shutil.rmtree(new_example_dir)
    
    ignore = shutil.ignore_patterns('.ipynb_checkpoints', '*.pyc', '*~')
    shutil.copytree(old_example_dir, path, ignore=ignore, symlinks=True)
    

def get_setup_version(root, reponame):
    """
    Helper to get the current version from either git describe or the
    .version file (if available) - allows for param to not be available.
    
    Normally used in setup.py as follows: 
    
    >>> from pyct.build import get_setup_version
    >>> version = get_setup_version(__file__, reponame)  # noqa
    """
    import json
    filepath = os.path.abspath(os.path.dirname(root))
    version_file_path = os.path.join(filepath, reponame, '.version')
    try:
        from param import version
    except:
        version = None
    if version is not None:
        return version.Version.setup_version(basepath, reponame, archive_commit="$Format:%h$")
    else:
        print("WARNING: param>=1.6.0 unavailable. If you are installing a package, this warning can safely be ignored. If you are creating a package or otherwise operating in a git repository, you should install param>=1.6.0.")
        return json.load(open(version_file_path, 'r'))['version_string']
    
