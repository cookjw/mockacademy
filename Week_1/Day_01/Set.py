from random import choice

class Set:
    def __init__(self, *items):
        self.items = {}
        self.array = []
        for item in items:
            self.add(item)
        
    def __repr__(self):
        return "Set: " + str(self.array)
        
    def add(self, item):
        self.array.append(item)
        self.items[item] = len(self.array) - 1
        
    def remove(self, item):
        index = self.items[item]
        last_item = self.array[-1]
        current_item = self.array[index]
        assert current_item == item
        self.array[index] = last_item
        self.items[last_item] = index
        self.array[-1] = current_item
        self.items[current_item] = len(self.array) - 1
        del self.array[-1]
        del self.items[item]
        
    def sample(self):
        return choice(self.array)