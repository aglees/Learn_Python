class BinaryTree(object):

    def __init__(self, obj):

        self.key = obj
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self, newNode):

        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRightChild(self, newNode):
        
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

def Preorder(tree):

    if tree != None:
        print(tree.getRootVal())
        Preorder(tree.getLeftChild())
        Preorder(tree.getRightChild())

def Inorder(tree):

    if tree != None:
        Preorder(tree.getLeftChild())
        print(tree.getRootVal())
        Preorder(tree.getRightChild())

def Postorder(tree):

    if tree != None:
        Preorder(tree.getLeftChild())
        Preorder(tree.getRightChild())
        print(tree.getRootVal())
        

btree = BinaryTree('root0')
btree.insertLeftChild('leftChild1')
btree.insertRightChild('rightChild1')
btree.rightChild.insertLeftChild('leftChild2')
btree.leftChild.insertLeftChild('leftChild2')
btree.leftChild.leftChild.insertLeftChild('leftChild3')
btree.leftChild.leftChild.insertRightChild('rightChild3')
btree.rightChild.insertRightChild('rightChild2')
btree.rightChild.rightChild.insertLeftChild('leftChild3')
btree.rightChild.rightChild.insertRightChild('rightChild3')

Postorder(btree)

del btree