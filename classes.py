class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            #removing the last element
            return self.items.pop()
        else:
            raise IndexError("Empty stack!")
        
    def is_empty(self):
        return len(self.items) == 0
    
    def length(self):
        return len(self.items)
    
    
    



    
