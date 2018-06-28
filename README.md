# pyct

A utility package that includes:

  1. **pyct.cmd**: Makes various commands available to other
     packages. (Currently no sophisticated plugin system, just a try
     import/except in the other packages.) The same commands are
     available from within python. Can either add new subcommands to
     an existing argparse based command if the module has an existing
     command, or create the entire command if the module has no
     existing command. Currently, there are commands for copying
     examples and fetching data. See

  2. **pyct.build**: Provides various commands to help package
     building, primarily as a convenience for project maintainers.

## pyct.cmd

To install pyct with the dependencies required for pyct.cmd: `pip
install pyct[cmd]` or `conda install -c pyviz pyct`.

An example of how to use in a project:
https://github.com/ioam/geoviews/blob/master/geoviews/__main__.py

Once added, users can copy the examples of a package and download the
required data with the `examples` command:

```
$ datashader examples --help
usage: datashader examples [-h] [--path PATH] [-v] [--force]

optional arguments:
  -h, --help     show this help message and exit
  --path PATH    location to place examples and data
  -v, --verbose
  --force        if PATH already exists, force overwrite existing examples if older than source examples
```

To copy the examples of e.g. datashader but not download the data,
there's a `copy-examples` command:

```
usage: datashader copy-examples [-h] [--path PATH] [-v] [--force]

optional arguments:
  -h, --help     show this help message and exit
  --path PATH    where to copy examples
  -v, --verbose
  --force        if PATH already exists, force overwrite existing examples if older than source examples
```

And to download the data only, the `fetch-data` command:

```
usage: datashader fetch-data [-h] [--path PATH] [--datasets DATASETS] [-v]

optional arguments:
  -h, --help           show this help message and exit
  --path PATH          where to put data
  --datasets DATASETS  *name* of datasets file; must exist either in path specified by --path or in package/examples/
  -v, --verbose
```

Can specify different 'datasets' file:

```
$ cat earthsim-examples/test.yml
---

data:

  - url: http://s3.amazonaws.com/datashader-data/Chesapeake_and_Delaware_Bays.zip
    title: 'Depth data for the Chesapeake and Delaware Bay region of the USA'
    files:
      - Chesapeake_and_Delaware_Bays.3dm

$ earthsim fetch-data --path earthsim-examples --datasets-filename test.yml
Downloading data defined in /tmp/earthsim-examples/test.yml to /tmp/earthsim-examples/data
Skipping Depth data for the Chesapeake and Delaware Bay region of the USA
```


## pyct.build

Currently provides a way to package examples with a project, by
copying an examples folder into the package directory whenever
setup.py is run. The way this works is likely to change in the near
future, but is provided here as the first step towards
unifying/simplifying the maintenance of a number of pyviz projects.
