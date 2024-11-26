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
    


def is_valid_string(s):

    stack = Stack()

    for char in s:

        #the stack contains only open brackets
        if char in "([{":
            stack.push(char)

        #if we got here we have a close bracket
        else:
            if stack.is_empty(): 
                return False
            top_element = stack.pop()
            if (char == ')' and top_element != '(') or \
               (char == '}' and top_element != '{') or \
               (char == ']' and top_element != '['):
                return False
            
    return stack.is_empty()

print(is_valid_string("(){}[]"))
print(is_valid_string("(){[]"))
print(is_valid_string("[(){}]"))

#should be true
print(is_valid_string(""))






