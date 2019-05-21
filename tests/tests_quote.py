import sys
import unittest

from stormbot import mock, bot
from stormbot_quote import Quote


class TestQuoteCommand(unittest.TestCase):
    @mock.bot(['quote'])
    @mock.storage({'quotes': {'author': ['quote']}})
    def test_one_quote(self, stdout):
        # When
        bot.main(Quote)

        # Then
        self.assertEqual(stdout.getvalue(), "author \"quote\"\n")

    @mock.bot(['quote', 'author', 'quote'])
    @mock.storage({'quotes': {}})
    def test_add_quote(self, stdout):
        # When
        bot.main(Quote)

        # Then
        self.assertEqual(stdout.getvalue(), "Your words are now engraved in the stones\n")


if __name__ == '__main__':
    unittest.main()
