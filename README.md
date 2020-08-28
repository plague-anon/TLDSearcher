![License](https://img.shields.io/github/license/plague-anon/tldsearcher) ![LastCommit](https://img.shields.io/github/last-commit/plague-anon/tldsearcher) ![os](https://img.shields.io/badge/Supported%20OS-GNU%2FLinux-blue) ![version](https://img.shields.io/github/v/release/plague-anon/TLDSearcher) ![wheel](https://img.shields.io/pypi/wheel/TLDSearcher) ![pythonversion](https://img.shields.io/pypi/pyversions/tldsearcher)

![tldSearcher Image](/imgs/tldsearcher.png)

# TLDSearcher
This Python tool searcher target domains for existing top-level domains _(TLDs)_

## Installation
**TLDSearcher** can be installed via [Github](https://github.com/plague-anon/TLDSearcher/) or [PyPI](https://pypi.org/project/tldsearcher/). Details on each are listed below.

### Github
Navigate to the directory where you want to download the program.

1. open a terminal and type:

> `git clone https://www.github.com/plague-anon/TLDSearcher`

2. Change into the directory git made for you:

> `cd TLDSearcher`

3. Run the following command to install the program:

> `python3 setup.py install`

You can now use the `tldsearcher` command from anywhere on your system


### PyPI
You can install **TLDSearcher** via pip with 2 methods.
**Method 1**
Issue the following command from the terminal to download the [latest version](https://pypi.org/project/tldsearcher/) from [pypi.org](https://pypi.org)

> `pip3 install tldsearcher`

**Method 2**
Issue the following command from the terminal to download the [latest version](https://github.com/plague-anon/TLDSearcher/releases) from [Github](https://www.github.com)

> `pip3 install -e git+https://github.com/plague-anon/TLDSearcher#egg=pkg`

## Usage Example
```
tldsearcher -t example -d com,co.uk,.net,.org -v
```
_The `-d` flag must be a string of TLDs, separated with a comma. The preceding `.` does not have to be supplied_

_For more examples and usage, please refer to the [Wiki][wiki]._


## Meta

plague – plague_anon@protonmail.com

Join me on the official Anonymous IRC webchat.anonops.com, or via an IRC client, irc.anonops.com:6697

Distributed under the GNU General Public License v3.0. See ``LICENSE`` for more information.

https://github.com/plague-anon/TLDSearcher

## Contributing

1. Fork it (<https://github.com/plague-anon/TLDSearcher>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


[wiki]: https://github.com/plague-anon/TLDSearcher/wiki
[gitRepo]: https://github.com/plague-anon/TLDSearcher
