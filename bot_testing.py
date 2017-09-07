"""
test suite for bot.py
"""
import unittest
import bot

""" tests the various methods in bot.py """
class TestBotMethods(unittest.TestCase):
#FIXME separate into multiple test cases with 1-2 asserts in each
    """ test censor() """
    def test_censor(self):
        #hell
        self.assertEqual(bot.censor("what the hell!"), "WHAT THE HECK!")
        self.assertEqual(bot.censor("this is a string"),"THIS IS A STRING")
        self.assertEqual(bot.censor("hell,,,,"), "HECK,,,,")
        self.assertEqual(bot.censor("hella cool !hell!"), "A HECKA LOTTA COOL !HECK!")
        self.assertEqual(bot.censor("hell o"), "HECK O")
        self.assertEqual(bot.censor("HELL"), "HECK")

        #hella
        self.assertEqual(bot.censor("hella"), "A HECKA LOTTA")

        #af
        #self.assertEqual(bot.censor("dank af"), "DANK AS FRICK")
        #self.assertEqual(bot.censor("after"), "AFTER") #FIXME

        #misc
        self.assertEqual(bot.censor("shitty fucking dicks"), "UNFORTUNATE IN A POOPY MANNER FRICKING LONG BOIS")
if __name__ == '__main__':
    unittest.main()
