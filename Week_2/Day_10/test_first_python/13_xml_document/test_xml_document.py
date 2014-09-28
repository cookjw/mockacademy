import unittest, xml_document, random, string

class TestXMLDocument(unittest.TestCase):
    def setUp(self):
        self.xml = xml_document.XMLDocument()
        
    def test_renders_empty_tag(self):
        self.assertEqual(self.xml.hello(), "<hello/>")
        
    def test_renders_tag_with_attributes(self):
        self.assertEqual(self.xml.hello({"name":"dolly"}), "<hello name='dolly'/>")
        
    def test_renders_randomly_named_tag(self):
        tag_name = ''.join([random.choice(string.lowercase) for x in range(9)])
        self.assertEqual(self.xml.send(tag_name), "<{0}/>".format(tag_name))
        
    def test_renders_block_with_text_inside(self):
        def f():
            return "dolly"
        self.assertEqual(self.xml.hello(function=f)(),"<hello>dolly</hello>")
        
    def test_nests_one_level(self):
        self.assertEqual(self.xml.hello(function=self.xml.goodbye)(),"<hello><goodbye/></hello>")
        
    def test_nests_several_levels(self):
        self.assertEqual(self.xml.hello(function=self.xml.goodbye(function=self.xml.come_back(function=self.xml.ok_fine({"be":"that_way"}))))(), "<hello><goodbye><come_back><ok_fine be='that_way'/></come_back></goodbye></hello>" )
        
    def test_indents(self):
        self.xml = xml_document.XMLDocument(True)
        self.assertEqual(self.xml.indents, True)
        self.assertEqual(self.xml.hello(function=self.xml.goodbye(function=self.xml.come_back(function=self.xml.ok_fine({"be":"that_way"}))))(), "<hello>\n" +
            "  <goodbye>\n" +
            "    <come_back>\n" +
            "      <ok_fine be='that_way'/>\n" +
            "    </come_back>\n" +
            "  </goodbye>\n" +
            "</hello>\n")    




if __name__ == "__main__":
    unittest.main()