![License](https://img.shields.io/github/license/plague-anon/tldsearcher) ![LastCommit](https://img.shields.io/github/last-commit/plague-anon/tldsearcher) ![os](https://img.shields.io/badge/Supported%20OS-GNU%2FLinux-blue) ![version](https://img.shields.io/github/v/release/plague-anon/TLDSearcher) ![wheel](https://img.shields.io/pypi/wheel/TLDSearcher) ![pythonversion](https://img.shields.io/pypi/pyversions/tldsearcher)

# TLDSearcher
> This Python tool searches given domains for any active top-level-domains(TLDs) also using the domain name.

Supplying 'example' as the target, and 'com,uk,net,org,biz' as the domains; tldsearcher will tell you if the domains are active or not.

## Installation
### Pypi
`pip install tldsearcher`

### Github
Clone the repository from Github
```
git clone https://github.com/plague-anon/TLDSearcher
```
Change into the directory
```
cd TLDSearcher
```
Run setup.py
```
python setup.py install
```
The installation process will create a link to your /usr/local/bin file and you can run the program from anywhere on your system by typing `tldsearcher`

## Usage Example
```
tldsearcher -t example -d com,co.uk,.net,.org -v
```
_The -d flag must be a string of TLDs, separated with a comma. The preceding '.' does not have to be supplied_

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
