import unittest
import bot

""" tests the various methods in bot.py """
class TestBotMethods(unittest.TestCase):

    """ test censor() """
    def test_censor(self):
        self.assertEqual(bot.censor("THIS IS A STRING"), ["this", "is", "a", "string"])

if __name__ == '__main__':
    unittest.main()
