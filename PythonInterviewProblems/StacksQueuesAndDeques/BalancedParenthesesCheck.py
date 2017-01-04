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

def balance_check(s):

    push_chars = ['{','(','['] 
    char_map = {']':'[',
                ')':'(',
                '}':'{' }

    if s[0] not in push_chars:
        return False

    stack = Stack()

    for item in s:

        if item in push_chars:
            stack.push(item)
        elif char_map[item] != stack.pop():
            return False

    return True 

# print (balance_check('[]'))

# print (balance_check('[](){([[[]]])}'))

print (balance_check('()(){]}'))
