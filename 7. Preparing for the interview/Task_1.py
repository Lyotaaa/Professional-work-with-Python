class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        lost_elem = self.stack.pop()
        return lost_elem

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
