import unittest
from simon_says import echo, shout, repeat, start_of_word, first_word, titleize

class SimonTest(unittest.TestCase):
    def test_echo(self):
        self.assertEqual(echo("hello"), "hello")
        self.assertEqual(echo("bye"), "bye")
        
    def test_shout(self):
        self.assertEqual(shout("hello"), "HELLO")
        self.assertEqual(shout("hello world"), "HELLO WORLD")
        
    def test_repeat(self):
        self.assertEqual(repeat("hello"), "hello hello")
        self.assertEqual(repeat("hello", 3), "hello hello hello")
        
    def test_start_of_word(self):
        self.assertEqual(start_of_word("hello", 1), "h")
        self.assertEqual(start_of_word("Bob", 2), "Bo")
        s = "abcdefg"
        self.assertEqual(start_of_word(s, 1), "a")
        self.assertEqual(start_of_word(s, 2), "ab")
        self.assertEqual(start_of_word(s, 3), "abc")
        
    def test_first_word(self):
        self.assertEqual(first_word("Hello World"), "Hello")
        self.assertEqual(first_word("oh dear"), "oh")
        
    def test_titelize(self):
        self.assertEqual(titleize("jaws"), "Jaws")
        self.assertEqual(titleize("david copperfield"), "David Copperfield")
        self.assertEqual(titleize("war and peace"), "War and Peace")
        self.assertEqual(titleize("the bridge over the river kwai"), "The Bridge over the River Kwai")


if __name__ == '__main__':
    unittest.main()             