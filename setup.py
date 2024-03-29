#!/usr/bin/env python3

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='stormbot-quote',
      version='2.0',
      description='store best quote easily from your Stormbot',
      long_description=long_description,
      author='Paul Fariello',
      author_email='paul@fariello.eu',
      url='https://github.com/manoir/stormbot-quote',
      packages=find_packages(exclude=["tests"]),
      test_suite="tests",
      install_requires=['stormbot>=2.0'],
      entry_points={'stormbot.plugins': ['quote = stormbot_quote:Quote']},
      classifiers=['Environment :: Console',
                   'Operating System :: POSIX',
                   'Topic :: Communications :: Chat',
                   'Programming Language :: Python'])
