#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

from tldsearcher.__init__ import __version__

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="plague",
    author_email='plague_anon@protonmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A tool for finding TLDs for domains",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='tldsearcher',
    name='tldsearcher',
    packages=find_packages(include=['tldsearcher', 'tldsearcher.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/plague-anon/tldsearcher',
    version=__version__,
    zip_safe=False,
)
