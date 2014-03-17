# Python tranlsation of exercises by Zack Davis and Ben Hass, App Academy Week 1
# Original at https://github.com/zackmdavis/App_Academy_Exercises/blob/master/Week_1/recursion.rb

def range1(first, last):
    if first == last:
        return [first]
    else:
        return [first] + range1(first + 1, last)
        
        
class Array(list):
    
    def sum_recursive(self):
        if len(self) == 0:
            return 0
        elif len(self) == 1:
            return self[0]
        else:
            L = Array()
            for n in range(1, len(self)):
                L.append(self[n])
            return self[0] + L.sum_recursive()
        
        
        

    def sum_iterative(self):
        sum = 0
        for n in self:
            sum += n
        return sum


def expt_dumb(base, exp):
    if exp == 0:
        return 1
    else:
        return base*expt_dumb(base, exp - 1)

def expt_smart(base, exp):
    # O(lg "exp") multiplications --- more efficient!
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        n = expt_smart(base, exp/2)
        return n*n
    else:
        n = expt_smart(base, (exp-1)/2)
        return base*n*n    


class Array(list):
    
    def deep_dup(self):
        arr = []
        for el in self:
            if type(el) == Array:
                arr.append(el.deep_dup())
            else:
                arr.append(el)            
        return arr
        
def fibs_recursive(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        prev = fibs_recursive(n-1)
        return prev + [prev[-1]+prev[-2]]
        
def fibs_iterative(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibs = [0, 1]
        k = 1
        while k <= n-2:
            fibs.append(fibs[-1] + fibs[-2])
            k += 1
        return fibs

        
def binary_search(array, first, last, target):
    middle = (last - first)/2 + first
    middle_val = array[middle]
    if middle_val == target:
        return middle
    elif middle_val < target:
        return binary_search(array, middle + 1, len(array) - 1, target)
    else:
        return binary_search(array, 0, middle, target)
        
        
def binary_search2(array, target):
    middle = len(array)/2
    middle_val = array[middle]
    if middle_val == target:
        return middle
    elif middle_val < target:
        return middle + 1 + binary_search2(array[middle + 1 : len(array)], target)
    else:
        return binary_search2(array[:middle], target)
        
        
def make_change(amount, denominations = [25, 10, 5, 1]):
    # take the largest element of denominations less or equal to than amount
    # appended with recursive call to same
    # this "greedy" algorithm gives correct change, but not optimal change
    if amount == 0:
        return []
    else:
        next_coin = [n for n in denominations if n <= amount][0]
        return [next_coin] + make_change(amount-next_coin)
        

        
def my_merge(left, right):
    merged = []
    while not (len(left) == 0 and len(right) == 0):
        if len(left) == 0 or len(right) == 0:
            merged += left + right
            return merged
        elif left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    return merged

def my_mergesort(self):
    if len(self) <= 1:
        return self
    else:
        middle = len(self)/2
        selftomiddle = Array()
        for x in self[:middle]:
            selftomiddle.append(x)
        left = selftomiddle.my_mergesort()
        selfmiddleon = Array()
        for x in self[middle:]:
            selfmiddleon.append(x)
        right = selfmiddleon.my_mergesort()
        return Array.my_merge(left, right)
    


Array.my_merge = staticmethod(my_merge)
Array.my_mergesort = my_mergesort  


def subsets(set):
    # P{S U {t}} = P{S} U {s U {t} | s >= P(S)}
    # id est, the powerset of the union of the set S and the singleton set {t} ...
    # equals the union of the powerset of S with
    # the sets s U {t} for all s in the the powerset of S
    if len(set) == 0:
        return [[]]
    else:   
        small = set[-1]
        return (subsets(set[:len(set)-1]) + 
            [s + [small] for s in subsets(set[:len(set)-1])])    



            
        

    
    
    
    
    
    
    
    
    
    
    
    


        
                
                
                    

    