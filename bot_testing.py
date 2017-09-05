import unittest
import bot

""" tests the various methods in bot.py """
class TestBotMethods(unittest.TestCase):

    """ test censor() """
    def test_censor(self):
        self.assertEqual(bot.censor("this is a string"),"THIS IS A STRING")
        self.assertEqual(bot.censor("what the hell!"), "WHAT THE HECK")

if __name__ == '__main__':
    unittest.main()
