

# from gitrecs import similarity

# assert similarity({}, {}) == 0.0
# assert similarity({'a', 'b'}, {'b', 'c', 'c'}) == 0.25
# assert similarity(['a', 'a'], ['a', 'b']) == 0.5


# from gitrecs import similarity

# def test_empty():
    # assert similarity({}, {}) == 0.0

# def test_sets():
    # assert similarity({'a', 'b'}, {'b', 'c', 'd'}) == 0.25
    
# def test_list_with_dupes():
    # assert similarity(['a', 'a'], ['a', 'b']) == 0.5
    
# if __name__ == '__main__':
    # for func in test_empty, test_sets, test_list_with_dupes:
        # try:
            # func()
        # except Exception as e:
            # print "{} FAILED: {}".format(func.__name__, e)
        # else:
            # print "{} passed.".format(func.__name__)

# from gitrecs import similarity            
            
# def test_empty():
    # assert similarity({}, {}) == 0.0

# def test_sets():
    # assert similarity({'a', 'b'}, {'b', 'c', 'd'}) == 0.25
    
# def test_list_with_dupes():
    # assert similarity(['a', 'a'], ['a', 'b']) == 0.5

    
import unittest   
from gitrecs import similarity

class TestSimilarity(unittest.TestCase):
    def test_empty(self):
        score = similarity({}, {})
        self.assertEqual(score, 0.0)
        
    def test_sets(self):
        score = similarity({'a'}, {'a', 'b'})
        self.assertEqual(score, 0.5)
        
    def test_list_with_dupes(self):
        score = similarity(['a', 'a'], ['a', 'b'])
        self.assertEqual(score, 0.5)
        
if __name__ == '__main__':
    unittest.main()

    