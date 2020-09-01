![License](https://img.shields.io/github/license/plague-anon/tldsearcher) ![LastCommit](https://img.shields.io/github/last-commit/plague-anon/tldsearcher) ![os](https://img.shields.io/badge/Supported%20OS-GNU%2FLinux-blue) ![version](https://img.shields.io/github/v/release/plague-anon/TLDSearcher) ![pythonversion](https://img.shields.io/pypi/pyversions/tldsearcher)

![tldSearcher Image](/imgs/tldsearcher.png)

# TLDSearcher
This Python tool searcher target domains for existing top-level domains _(TLDs)_

Knowing which TLDs are active for a specific domain can be a helpful tool in reconnaissance during a scan. Instead of Google-dorking, and let's face it - failing to get enough results, use **TLDSearcher** to check **ALL**, currently available TLDs on the web.

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
You can install **TLDSearcher** via pip
**Method 1**
Issue the following command from the terminal to download the [latest version](https://pypi.org/project/tldsearcher/) from [pypi.org](https://pypi.org)

> `pip3 install tldsearcher`


## Usage Examples
To verbosely search for **all** TLDs for _example_:
`tldsearcher -t example -v`

To verbosely search for specific TLDs for _example_ and output into _scan.txt_:
`tldsearcher -t example -d com,net,info,org -o scan.txt -v `

To see a list of TLD categories to scan for _example_:
`tldSearcher -t example -dC -o scan.txt -v`

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
