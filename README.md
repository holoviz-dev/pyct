**Experimental**

A 'pyviz cmd util' package that when installed makes
`install_examples` and `download_data` commands available to other
packages. (No sophisticated plugin system, just a try import/except in
the other packages.) The same commands are available from within
python for users, too. Can either add new subcommands to existing
argparse based command if module has existing command, or create the
entire command if module has no existing command.

Examples...

```
$ datashader download_data
usage: datashader download_data [-h]
datashader download_data: error: install examples package to enable this command (`conda install datashader-examples`)
$ conda install -c pyviz pvutil
[...]
$ datashader install_examples
Installed examples at /tmp/datashader-examples
$ python -c "import datashader; datashader.install_examples('test123')"
Installed examples at /tmp/test123
```


```
$ earthsim
usage: earthsim [-h] [--version] {install_examples,download_data} ...
earthsim: error: must supply command to run

$ earthsim --version
earthsim 1.0.2a0.post26+g9212df2

$ earthsim install_examples --help
usage: earthsim install_examples [-h] [--path PATH] [--include-data] [-v]

optional arguments:
  -h, --help      show this help message and exit
  --path PATH     where to install examples
  --include-data  also download data (see download_data command for more flexibility)
  -v, --verbose
```

Can install examples alone:
```
$ rm -rf earthsim-examples/
$ earthsim install_examples --path=earthsim-examples
Installed examples at /tmp/earthsim-examples
$ ls earthsim-examples/
conftest.py  datasets.yml  topics  user_guide  README.md
```

Or install examples and download data:
```
$ rm -rf earthsim-examples/
$ earthsim install_examples --path=earthsim-examples --include-data
Installed examples at /tmp/earthsim-examples
Downloading data defined in /tmp/earthsim-examples/datasets.yml to /tmp/earthsim-examples/data
Downloading Depth data for the Chesapeake and Delaware Bay region of the USA 1 of 1
[################################] 20444/20444 - 00:00:05
Downloading SanDiego mesh data and AdH model output 1 of 1
[################################] 26161/26161 - 00:00:04
Downloading Vicksburg watershed shapefile used as GSSHA simulation input 1 of 1
[################################] 4/4 - 00:00:00
$ ls earthsim-examples/
conftest.py  data  datasets.yml  topics  user_guide  README.md
```

Currently, re-running the command will 'update' any installed example
older than the source (think will change to never overwrite instead).

```
$ earthsim install_examples --path=earthsim-examples --include-data
Path /tmp/earthsim-examples already exists; will only overwrite older target files.
Installed examples at /tmp/earthsim-examples
Downloading data defined in /tmp/earthsim-examples/datasets.yml to /tmp/earthsim-examples/data
Skipping Depth data for the Chesapeake and Delaware Bay region of the USA
Skipping SanDiego mesh data and AdH model output
Skipping Vicksburg watershed shapefile used as GSSHA simulation input
```


Can also download data alone:

```
$ earthsim download_data --help
usage: earthsim download_data [-h] [--path PATH] [--datasets-filename DATASETS_FILENAME] [-v]

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           where to download data
  --datasets-filename DATASETS_FILENAME
                        something
  -v, --verbose

$ earthsim download_data --path earthsim-examples
Downloading data defined in /tmp/earthsim-examples/datasets.yml to /tmp/earthsim-examples/data
Skipping Depth data for the Chesapeake and Delaware Bay region of the USA
Skipping SanDiego mesh data and AdH model output
Skipping Vicksburg watershed shapefile used as GSSHA simulation input
```


Can specify different 'datasets' file:

```
$ cp earthsim-examples/datasets.yml earthsim-examples/test.yml
$ # (edit test.yaml)
$ cat earthsim-examples/test.yml
---

data:

  - url: http://s3.amazonaws.com/datashader-data/Chesapeake_and_Delaware_Bays.zip
    title: 'Depth data for the Chesapeake and Delaware Bay region of the USA'
    files:
      - Chesapeake_and_Delaware_Bays.3dm

$ earthsim download_data --path earthsim-examples --datasets-filename test.yml
Downloading data defined in /tmp/earthsim-examples/test.yml to /tmp/earthsim-examples/data
Skipping Depth data for the Chesapeake and Delaware Bay region of the USA
```

If there's no datasets-filename in the specified path, looks for it in the package (in package/examples/):

```
$ rm earthsim-examples/datasets.yml
$ earthsim download_data --path earthsim-examples
Downloading data defined in /EarthSim/earthsim/examples/datasets.yml to /tmp/earthsim-examples/data
Skipping Depth data for the Chesapeake and Delaware Bay region of the USA
Skipping SanDiego mesh data and AdH model output
Skipping Vicksburg watershed shapefile used as GSSHA simulation input
```
