class Dictionary(dict): # theoretically cheating to inherit from dict, but not really wrong in this case
    
    def __init__(self):
        self.entries = self
        
    def add(self, entry):
        if hasattr(entry, 'keys'):
            self[entry.keys()[0]] = entry[entry.keys()[0]]
        else:
            self[entry] = None
            
    def keywords(self):
        return sorted(self.keys())
        
    def find(self, word):
        results = {}
        for key in self.entries:
            if word in key:
                results[key] = self[key]
        return results
        
    def printable(self):
        output = ""
        for entry in sorted(self.entries)[:-1]:
            output = output + "[" + entry + "]" + " " + "\"" + self[entry] + "\"" +"\n"
        output = output + "[" + sorted(self.entries)[-1] + "]" + " " + "\"" + self[sorted(self.entries)[-1]] + "\"" 
        return output
        
            
                    