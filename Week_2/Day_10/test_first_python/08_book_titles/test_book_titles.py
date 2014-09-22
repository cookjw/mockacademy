import unittest
from book import Book


class BookTest(unittest.TestCase):       
    def test_capitalize_first_letter(self):
        book = Book("inferno")
        # book.title = "inferno"
        self.assertEqual(book.get_title(), "Inferno")
        
    def test_capitalize_every_word(self):
        book = Book("stuart little")
        self.assertEqual(book.get_title(), "Stuart Little")
        
    def test_capitalize_every_word_except(self):
        def correction(title, correct_title):
            book = Book(title)
            self.assertEqual(book.get_title(), correct_title)
        correction("alexander the great", "Alexander the Great")        
        correction("to kill a mockingbird", "To Kill a Mockingbird")
        correction("to eat an apple a day", "To Eat an Apple a Day")
        correction("war and peace", "War and Peace")
        correction("love in the time of cholera","Love in the Time of Cholera")
        correction("what i wish i knew when i was 20", "What I Wish I Knew When I Was 20")
        correction("the man in the iron mask", "The Man in the Iron Mask")
        

                               
        
        
        

if __name__ == "__main__":
    unittest.main()