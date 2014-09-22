class Book():
    def __init__(self, name):
        namewords = name.split(' ')
        capname = [] 
               
        for index in range(len(namewords)):
            word = namewords[index]
            if not (word in ["and", "the", "in", "an", "or", "at", "of", "a", "over"] and index != 0):
                word = word.title()
            capname.append(word)
        self.name = ' '.join(capname)
    
    def get_title(self):
        return self.name
        
    # def make_title(self, name):
        # namewords = name.split(' ')
        # capname = []   
        # for index in range(len(namewords)):
            # word = namewords[index]
            # if not (word in ["and", "the", "in", "an", "or", "at", "of", "a", "over"] and index != 0):
                # word.title()
            # capname.append(word)
        # self.name = ' '.join(capname)