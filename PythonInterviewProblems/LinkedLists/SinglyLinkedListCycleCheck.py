class Node(object):
    
    def __init__(self, value):
        
        self.value = value
        self.nextnode = None

# this only checks if the list links back to the start 
# it won't detect intra-list cycles
def cycle_check(node):
    
    if node.nextnode == None:
        return False
    
    original_node = node
    next_node = original_node.nextnode
        
    while next_node != None:
        
        if next_node.nextnode == None:
            return False
        elif next_node == original_node:
            return True
        
        next_node = next_node.nextnode

# write a better function using the 2-runners idea
def cycle_check2(node):
    pass

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print "ALL TEST CASES PASSED"
        
# Run Tests

t = TestCycleCheck()
t.test(cycle_check)
