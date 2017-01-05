class Queue2Stacks(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, element):
        
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            self.stack1.append(element)
        elif len(self.stack1) == 1:
            self.stack2.append(element)
        else:
            self.stack1.append(element)

    def dequeue(self):
        
        item = self.stack1.pop()

        while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())
        
        if len(self.stack1) > 0:
            nextpop = self.stack1.pop()

            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

            self.stack1.append(nextpop)

        return item

class Queue2Stacks2(object):

    def __init__(self):
        self.instack = []
        self.outstack = []
    
    def enqueue(self, element):
        
        self.instack.append(element)
        
    def dequeue(self):
        
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
    
        return self.outstack.pop()
