import unittest, dictionary

class DictionaryTest(unittest.TestCase):
    def setUp(self):
        self.d = dictionary.Dictionary()
        
    # def tearDown(self):
        # del d
        
    def test_00_empty_when_created(self):
        self.assertEqual(self.d.entries, {})
        
    def test_01_add_whole_entries_keyword_definition(self):
        self.d.add({'fish':'acquatic animal'})
        self.assertEqual(self.d.entries, {'fish':'acquatic animal'} )
        self.assertEqual(self.d.keywords(), ['fish'])
        
        
    def test_02_add_keyword_without_definition(self):        
        self.d.add('fish')
        self.assertEqual(self.d.entries, {'fish': None} )
        self.assertEqual(self.d.keywords(), ['fish'])
        
        
    def test_03_check_whether_keyword_exists(self):        
        self.assertNotIn('fish', self.d)
        
    def test_04_doesnt_cheat_when_checking_keyword_existence(self):
        self.assertNotIn('fish', self.d)
        self.d.add('fish')
        self.assertIn('fish', self.d)
        self.assertNotIn('bird', self.d)
        
        
    def test_05_doesnt_include_prefix(self):        
        self.d.add('fish')
        self.assertNotIn('fi', self.d)        
        
    def test_06_doesnt_find_word_empty_dictionary(self):
        self.assertEqual(self.d.find('fi'), {})
        
    def test_07_finds_nothing_if_prefix_matches_nothing(self):
        self.d.add('fiend')
        self.d.add('great')
        self.assertEqual(self.d.find('nothing'), {})
        
    def test_08_finds_an_entry(self):
        self.d.add({'fish':'acquatic animal'})
        self.assertEqual(self.d.find('fi'), {'fish':'acquatic animal'})
        
    def test_09_finds_multiple_matches_from_prefix(self):
        self.d.add({'fish':'acquatic animal'})
        self.d.add({'fiend':'wicked person'})
        self.d.add({'great':'remarkable'})
        self.assertEqual(self.d.find('fi'), {'fish':'acquatic animal', 'fiend':'wicked person'})
        
    def test_10_lists_keywords_alphabetically(self):
        self.d.add({'zebra': 'African land animal with stripes'})
        self.d.add({'fish': 'aquatic animal'})
        self.d.add({'apple': 'fruit'})    
        self.assertEqual(self.d.keywords(), ['apple', 'fish', 'zebra'])  

    def test_11_produce_printable_output(self):
        self.d.add({'zebra': 'African land animal with stripes'})
        self.d.add({'fish': 'aquatic animal'})
        self.d.add({'apple': 'fruit'})  
        self.assertEqual(self.d.printable(), "[apple] \"fruit\"\n[fish] \"aquatic animal\"\n[zebra] \"African land animal with stripes\"")


        
        
        
        
        
        
    









if __name__ == "__main__":
    unittest.main()