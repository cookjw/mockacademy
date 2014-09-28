import unittest
from in_words import in_words

class InWordsTest(unittest.TestCase):
    def test_reads_0_to_9(self):
        self.assertEqual(in_words(0),'zero')
        self.assertEqual(in_words(1),'one')
        self.assertEqual(in_words(2),'two')
        self.assertEqual(in_words(3),'three')
        self.assertEqual(in_words(4),'four')
        self.assertEqual(in_words(5),'five')
        self.assertEqual(in_words(6),'six')
        self.assertEqual(in_words(7),'seven')
        self.assertEqual(in_words(8),'eight')
        self.assertEqual(in_words(9),'nine')
        
    def test_reads_10_to_12(self):
        self.assertEqual(in_words(10),'ten')
        self.assertEqual(in_words(11),'eleven')
        self.assertEqual(in_words(12),'twelve')
        
    def test_reads_teens(self):
        self.assertEqual(in_words(13),'thirteen')
        self.assertEqual(in_words(14),'fourteen')
        self.assertEqual(in_words(15),'fifteen')
        self.assertEqual(in_words(16), 'sixteen')
        self.assertEqual(in_words(17), 'seventeen')
        self.assertEqual(in_words(18), 'eighteen')
        self.assertEqual(in_words(19), 'nineteen')
        
    def test_reads_tens(self):
        self.assertEqual(in_words(20), 'twenty')
        self.assertEqual(in_words(30), 'thirty')
        self.assertEqual(in_words(40), 'forty')
        self.assertEqual(in_words(50), 'fifty')
        self.assertEqual(in_words(60), 'sixty')
        self.assertEqual(in_words(70), 'seventy')
        self.assertEqual(in_words(80), 'eighty')
        self.assertEqual(in_words(90), 'ninety')
        
    def test_reads_various_under_100(self):
        self.assertEqual(in_words(20), 'twenty')
        self.assertEqual(in_words(77), 'seventy seven')
        self.assertEqual(in_words(99), 'ninety nine')
        
    def test_reads_hundreds(self):
        self.assertEqual(in_words(100), 'one hundred')
        self.assertEqual(in_words(200), 'two hundred')
        self.assertEqual(in_words(300), 'three hundred')
        self.assertEqual(in_words(123), 'one hundred twenty three')
        self.assertEqual(in_words(777), 'seven hundred seventy seven')
        self.assertEqual(in_words(818), 'eight hundred eighteen')
        self.assertEqual(in_words(512), 'five hundred twelve')
        self.assertEqual(in_words(999), 'nine hundred ninety nine')
        
    def test_reads_thousands(self):
        self.assertEqual(in_words(1000), 'one thousand')
        self.assertEqual(in_words(32767),'thirty two thousand seven hundred sixty seven' )
        self.assertEqual(in_words(32768), 'thirty two thousand seven hundred sixty eight')
        
    def test_reads_millions(self):
        self.assertEqual(in_words(10000001), 'ten million one')
        
    def test_reads_billions(self):
        self.assertEqual(in_words(1234567890), 'one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety')
        
    def test_reads_trillions(self):
        self.assertEqual(in_words(1000000000000), 'one trillion')
        self.assertEqual(in_words(1000000000001), 'one trillion one')
        self.assertEqual(in_words(1888259040036), 'one trillion eight hundred eighty eight billion two hundred fifty nine million forty thousand thirty six')
        
        






if __name__ == "__main__":
    unittest.main()