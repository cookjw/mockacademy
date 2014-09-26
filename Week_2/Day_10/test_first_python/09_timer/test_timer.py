import unittest, timer


class TestTimer(unittest.TestCase):
    def setUp(self):
        self.timer = timer.Timer()
        
    def test_initialize(self):
        self.assertEqual(self.timer.seconds, 0)
    
    def test_0_seconds(self):
        self.timer.seconds = 0
        self.assertEqual(self.timer.time_string(),"00:00:00") 
        
    def test_12_seconds(self):
        self.timer.seconds = 12
        self.assertEqual(self.timer.time_string(), "00:00:12")
        
    def test_66_seconds(self):
        self.timer.seconds = 66
        self.assertEqual(self.timer.time_string(), "00:01:06")
        
    def test_4000_seconds(self):
        self.timer.seconds = 4000
        self.assertEqual(self.timer.time_string(), "01:06:40")








if __name__ == "__main__":
    unittest.main()