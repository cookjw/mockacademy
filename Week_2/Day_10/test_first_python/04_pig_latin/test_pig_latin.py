import unittest
from pig_latin import translate

class PigLatinTest(unittest.TestCase):
    def test_translate(self):
        self.assertEqual(translate("apple"), "appleay")
        self.assertEqual(translate("banana"),"ananabay")
        self.assertEqual(translate("cherry"),"errychay")
        self.assertEqual(translate("eat pie"), "eatay iepay")
        self.assertEqual(translate("three"),"eethray")
        self.assertEqual(translate("school"),"oolschay")
        self.assertEqual(translate("quiet"), "ietquay")
        self.assertEqual(translate("square"), "aresquay")
        self.assertEqual(translate("the quick brown fox"),"ethay ickquay ownbray oxfay")
        self.assertEqual(translate("the quick brown Fox"), ("ethay ickquay ownbray Oxfay"))
        self.assertEqual(translate("the quick, brown...Fox!"), ("ethay ickquay, ownbray...Oxfay!"))
        




if __name__ == "__main__":
    unittest.main()