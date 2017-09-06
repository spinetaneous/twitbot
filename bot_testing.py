"""
test suite for bot.py
"""
import unittest
import bot

""" tests the various methods in bot.py """
class TestBotMethods(unittest.TestCase):

    """ test censor() """
    def test_censor(self):
        #censor hell
        self.assertEqual(bot.censor("what the hell!"), "WHAT THE HECK!")
        self.assertEqual(bot.censor("this is a string"),"THIS IS A STRING")
        self.assertEqual(bot.censor("hell,,,,"), "HECK,,,,")
        self.assertEqual(bot.censor("hella cool !hell!"), "HECKA COOL !HECK!")
        self.assertEqual(bot.censor("hell o"), "HECK O")
        self.assertEqual(bot.censor("HELL"), "HECK")

if __name__ == '__main__':
    unittest.main()
