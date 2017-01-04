class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()

print (s.size())

s.push(1)
s.push('two')
s.push(True)

print(s.peek())
print(s.pop())
print(s.size())
print(s.pop())
print(s.pop())
print(s.size())
