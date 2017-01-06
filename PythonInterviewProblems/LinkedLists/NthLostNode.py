class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def nth_to_last_node(n, head):

    # let's try a two-runner solution
    leader = head
    runner = head
    i = 0

    while True:

        #start leader
        leader = leader.nextnode

        if i > n-1:
            runner = runner.nextnode

        i += 1

        if leader == None:
            return runner

def nth_to_last_node2(n, head):

    left_pointer = head
    right_pointer = head

    for i in range(n-1):

        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than linked list')

        right_pointer  = right_pointer.nextnode

    while right_pointer.nextnode:

        left_pointer = left_pointer.nextnode

        right_pointer = right_pointer.nextnode

    return left_pointer

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node2(3, a)

print(target_node.value)