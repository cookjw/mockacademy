import datetime, time

def measure(function, timescount = 1):
    timings = []
    for index in range(timescount):
        start = time.time()
        function()
        finish = time.time()
        timings.append(finish - start)
    sum = 0.0  
    for number in timings:
        sum = sum + number
    return sum / timescount