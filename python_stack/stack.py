class Stack:

    def __init__(self):
        self.elements = []

    def insert(self, value):
        self.elements.append(value)
    
    def poll(self):
        return self.elements[-1]

    def pop(self):
        return self.elements.pop()