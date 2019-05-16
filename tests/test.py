import sys
from stormbot import storage, bot
from stormbot_quote import Quote
from unittest.mock import patch
from nose.tools import *
import logging

@bot.mock(['quote', '-h'])
@storage.mock({'quotes': {'author': ['quote']}})
def test_help(stdout):
    # When
    bot.main(Quote)

    # Then
    eq_(stdout.getvalue(), """usage: quote [-h] [--quote-cache QUOTE_CACHE] [_ [_ ...]]

positional arguments:
  _

optional arguments:
  -h, --help            show this help message and exit
  --quote-cache QUOTE_CACHE
                        Cache file (default: /var/cache/stormbot/quote.p)
author \"quote\"
""")

@bot.mock(['quote'])
@storage.mock({'quotes': {'author': ['quote']}})
def test_one_quote(stdout):
    # When
    bot.main(Quote)

    # Then
    eq_(stdout.getvalue(), "author \"quote\"\n")

@bot.mock(['quote', 'author', 'quote'])
@storage.mock({'quotes': {}})
def test_add_quote(stdout):
    # When
    bot.main(Quote)

    # Then
    eq_(stdout.getvalue(), "Your words are now engraved in the stones\n")


if __name__ == '__main__':
    import nose
    nose.runmodule()
