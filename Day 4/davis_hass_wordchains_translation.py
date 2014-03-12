# Python translation of Word Chains by Zack Davis and Ben Hass, App Academy Week 1
# Original at https://github.com/zackmdavis/App_Academy_Exercises/blob/master/Week_1/word_chains.rb


def adjacent(word1, word2):
    if not len(word1) == len(word2):
        return False
    matches = 0
    for i in range(len(word2)):
        if word1[i] == word2[i]:
            matches += 1
    if len(word2) - matches == 1:
        return True
    else:
        return False
            
            
            
class WordChains:

    def __init__(self):    
        self.dictionary = [word[:-1] for word in open("..\Day 3\dictionary.txt").readlines()]
    
    def adjacent_words(self, word):
        return [other_word for other_word in self.dictionary if adjacent(other_word, word)]
        
    
    def find_chain(self, start, target):
        found = False
        scanned = []
        to_scan = []
        to_scan.append({start : None})
        while (not to_scan == []) and (not found):
            scanning = to_scan.pop(0)            
            if scanning.keys()[0] == target:
                found = True                
                scanned.append(scanning)
            else:
                for adj_word in self.adjacent_words(scanning.keys()[0]):
                    if not adj_word in scanned and not adj_word in to_scan:
                        to_scan.append({adj_word : scanning.keys()[0]})
                scanned.append(scanning)
        if found:
            return self.__construct_path(target, scanned)
        
            
    def __construct_path(self, target, scanned):
        chain = [target]
        backlink = [h for h in scanned if h.keys()[0] == target][0]
        parent = backlink[target]
        while not parent == None:
            chain.append(parent)
            backlink = [h for h in scanned if h.keys()[0] == parent][0]
            parent = backlink[parent]
        return chain[::-1]
            
        
                 
            
    
    
    
    
    
    
    
    
    
    
wc = WordChains()

  

path = wc.find_chain("bunt", "tint") 
print path 
        
        