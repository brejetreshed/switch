class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            #removing the first element
            return self.items.pop(0)
        else:
            raise IndexError("Empty queue!")

    def is_empty(self):
        return len(self.items) == 0
    
    def length(self):
        return len(self.items)