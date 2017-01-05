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
    
    def isEmpty(self):
        return self.items == []

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
        elif stack.isEmpty():
            return False
        elif char_map[item] != stack.pop():
            return False

    return stack.isEmpty() 

# print (balance_check('[]'))

# print (balance_check('[](){([[[]]])}'))

print (balance_check('()(){]}'))

def balance_check2(s):

    if len(s) % 2 != 0:
        return False
    
    opening = set('([{')

    matches = set([ ('(', ')'), ('{', '}'), ('[', ']') ])

    stack = []

    for paren in s:

        if paren in opening:
            stack.append(paren)

        else:

            if len(stack) == 0:
                return False
            
            last_open = stack.pop()

            if (last_open,paren) not in matches:
                return False
            
    return len(stack) == 0
            
# print (balance_check('[]'))

# print (balance_check('[](){([[[]]])}'))

print (balance_check('()(){]}'))
