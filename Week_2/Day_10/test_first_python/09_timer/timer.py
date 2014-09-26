def timer(seconds):
    def hours(seconds):
        return seconds/3600
        
    def minutes(seconds):
        return (seconds / 60) % 60
        
    def numseconds(seconds):
        return seconds - hours(seconds)*3600 - minutes(seconds)*60

    def pad(two_digit_number): # in the sense of 0 < digits <= 2
        if len(str(two_digit_number)) == 1:
           one_digit_number = str(two_digit_number)
           return "0" + one_digit_number
        elif len(str(two_digit_number)) == 2:
            return str(two_digit_number)
        else:
            other_number = str(two_digit_number)
            return other_number
            
    return pad(str(hours(seconds))) + ":" + pad(str(minutes(seconds))) + ":" + pad(str(numseconds(seconds)))   
         

class Timer:
    def __init__(self):
        self.seconds = 0
        
    def time_string(self):
        return timer(self.seconds)
        