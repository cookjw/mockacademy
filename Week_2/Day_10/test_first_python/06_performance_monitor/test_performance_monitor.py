import unittest, datetime, mock, random, time
from performance_monitor import measure

ELEVEN_AM = time.mktime((datetime.datetime.strptime("2011-1-2 11:00:00", "%Y-%m-%d %H:%M:%S")).timetuple())
# courtesy of http://stackoverflow.com/questions/8022161/python-converting-from-datetime-datetime-to-time-time

faketime = ELEVEN_AM

def fake_time():
    return faketime

class PerformanceMonitorTest(unittest.TestCase):    
    def test_measure_01(self):    # it should take about 0 seconds to execute an empty function  
        def f():
            pass
        elapsed_time = measure(f)
        self.assertAlmostEqual(elapsed_time, 0.0, 1) 
    
    @mock.patch('time.time', fake_time)  # it should take exactly 0 seconds to execute an empty function (with mock) 
    def test_measure_02_with_mock(self):        
        def f():
            pass
        elapsed_time = measure(f)
        self.assertEqual(elapsed_time, 0.0)        
    
        
    def test_measure_03_sleep(self):   # it should take about 1 second to execute a function that sleeps for 1 second
        def f():
            time.sleep(1)
        elapsed_time = measure(f)
        self.assertAlmostEqual(elapsed_time, 1.0, 1)
        
        
    @mock.patch('time.time', fake_time)        # it should take exactly 1 second to run a block that sleeps for 1 second (with mock)
    def test_measure_04_sleep_with_mock(self):
        def f():            
            global faketime
            faketime = ELEVEN_AM
            faketime += 1               
        elapsed_time = measure(f)
        self.assertEqual(elapsed_time, 1)  

    def test_measure_05_run_block(self): # it should execute a function N times
        n = [0]
        def f():
            n[0] += 1
        measure(f, 4)
        self.assertEqual(n[0], 4)        
        
    @mock.patch('time.time', fake_time)    
    def test_measure_06_average_value(self): # it should return the average time, not the total time, when running multiple times
        run_times = [8,6,5,7]      
        global faketime
        faketime = ELEVEN_AM        
        def f():
            global faketime
            faketime += run_times.pop()
        average_time = measure(f, 4)
        self.assertEqual(average_time, 6.5)
        

    @mock.patch('time.time', fake_time)
    def test_measure_07_average_value(self): # it should return the average time when running a random number of times for random lengths of time
        global faketime
        faketime = ELEVEN_AM
        number_of_times = random.randrange(10) + 2
        def f():
            delay = random.randrange(10)
            global faketime
            faketime += delay
        average_time = measure(f, number_of_times)
        self.assertEqual(average_time, float(faketime - ELEVEN_AM)/number_of_times)                 


if __name__ == '__main__':
    unittest.main()     