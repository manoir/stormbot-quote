import sys
import unittest

from unittest.mock import patch
from stormbot import mock
from stormbot_quote import Quote


class TestQuoteCommand(unittest.TestCase):
    def test_no_quote(self):
        # Given
        with patch('stormbot_quote.Storage', mock.Storage()) as storage:
            bot = mock.bot(Quote)

            # When
            bot.command("stormbot: quote")

        # Then
        bot.send_message.assert_called_with(mbody="We don't have any quote yet, feel free to add some.",
                                            mto=bot.room, mtype="groupchat")

    def test_one_quote(self):
        # Given
        with patch('stormbot_quote.Storage', mock.Storage()) as storage:
            storage['quotes'] = {'author': ['quote']}
            bot = mock.bot(Quote)

            # When
            bot.command("stormbot: quote")

        # Then
        bot.send_message.assert_called_with(mbody="author \"quote\"",
                                            mto=bot.room, mtype="groupchat")

    def test_add_quote(self):
        # Given
        with patch('stormbot_quote.Storage', mock.Storage()) as storage:
            bot = mock.bot(Quote)

            # When
            bot.command("stormbot: quote author \"My wonderful quote\"")

        # Then
        bot.send_message.assert_called_with(mbody="Your words are now engraved in the stones",
                                            mto=bot.room, mtype="groupchat")
        self.assertIn('quotes', storage)
        self.assertIn('author', storage['quotes'])
        self.assertEqual(storage['quotes']['author'], ["My wonderful quote"])


if __name__ == '__main__':
    unittest.main()
