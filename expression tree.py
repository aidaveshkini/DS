from collections import deque

# Represents a node of the required tree✅
class ExprssionTree_node:
	def __init__(self,data):
		self.data=data
		self.left=self.right=None
class Expression_Tree:
    def __init__(self):
        self.root = None

# Function to print the infix expression for the tree🟥
    def inordertraverse(self): #recursion
        p = self.root
        if (p == None):
            return
        else:
            self.inordertraverse(p.left)
            print(p.data,end=' ')
            self.inordertraverse(p.right)

# Function to print the postfix expression for the tree✅
    def postordertraverse(self): #recursion
        p = self.root
        if (p == None):
            return
        else:
            subtree1 = Expression_Tree()
            subtree1.root= self.root.left
            subtree2 = Expression_Tree()
            subtree2.root= self.root.right
            subtree1.postordertraverse()
            subtree2.postordertraverse()
            print(p.data,end=' ')

# Function to print the prefix expression for the tree🟥
    def preordertraverse(self): #recursion
        p = self.root
        if (p == None):
            return 
        else:
            print(p.data,end=' ')
            self.preordertraverse(p.left)
            self.preordertraverse(p.right)

def postfix_to_tree(expr):#✅
 
    # base case
    if not expr:
        return
 
    # create an empty stack to store tree pointers
    s = deque()
 
    # traverse the postfix expression
    for c in expr:
        # if the current token is an operator
        if c == '+' or c == '-' or c == '*' or c == '/' or c == '^':
            # pop two nodes `x` and `y` from the stack
            x = s.pop()
            y = s.pop()
 
            # construct a new binary tree whose root is the operator and whose
            # left and right children point to `y` and `x`
            Nodee = ExprssionTree_node(c)
            Nodee.left = y
            Nodee.right = x

 
            # push the current node into the stack
            s.append(Nodee)
 
        # if the current token is an operand, create a new binary tree node
        # whose root is the operand and push it into the stack
        else:
            s.append(ExprssionTree_node(c))
 
    # a pointer to the root of the expression tree remains on the stack
    tree = Expression_Tree()
    tree.root = s[-1]
    return tree





tree = prefix



#tree = postfix_to_tree('ab+')
#tree.postordertraverse()


# (3+((5+9)*2)