import unittest
from friend import Friend

class FriendTest(unittest.TestCase):
    def test_hello(self):        
        self.assertEqual(Friend().greeting(), "Hello!")
        
    def test_hello_to_someone(self):
        self.assertEqual(Friend().greeting("Bob"), "Hello, Bob!")

if __name__ == '__main__':
    unittest.main()        