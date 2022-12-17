# program to construct an expression tree
from collections import deque


# Represents a node of the required tree
class node:
	def __init__(self,c):
		self.data=c
		self.left=self.right=None

# Function to recursively build the expression tree
def prefix_to_tree(a):
	#base case
	# If its the end of the expression
	if (a == ''):
		return ''

	# If the character is an operand
	if a[0]>='a' and a[0]<='z':
		return node(a[0]),a[1:]
	else:
		# Create a node with a[0] as the data and
		# both the children set to null
		p=node(a[0])
		# Build the left sub-tree
		p.left,q=prefix_to_tree(a[1:])
		# Build the right sub-tree
		p.right,q=prefix_to_tree(q)
		return p,q


# Function to construct an expression tree from the given postfix expression
def postfix_to_tree(a):
 
    # base case
    if not a:
        return
 
    # create an empty stack to store tree pointers
    s = deque()
 
    # traverse the postfix expression
    for c in a:
        # if the current token is an operator
        if c == '+' or c == '-' or c == '*' or c == '/' or c == '^':
            # pop two nodes `x` and `y` from the stack
            x = s.pop()
            y = s.pop()
 
            # construct a new binary tree whose root is the operator and whose
            # left and right children point to `y` and `x`
            Nodee = node(c)
            Nodee.left = y
            Nodee.right = x

 
            # push the current node into the stack
            s.append(Nodee)
 
        # if the current token is an operand, create a new binary tree node
        # whose root is the operand and push it into the stack
        else:
            s.append(node(c))
 
    # a pointer to the root of the expression tree remains on the stack
    return s[-1]


# Function to print the infix expression for the tree
def inordertraverse(p): #recursion

	if (p == None):
		return
	else:
		inordertraverse(p.left)
		print(p.data,end=' ')
		inordertraverse(p.right)

# Function to print the postfix expression for the tree
def postordertraverse(p): #recursion

	if (p == None):
		return
	else:
		postordertraverse(p.left)
		postordertraverse(p.right)
		print(p.data,end=' ')

# Function to print the prefix expression for the tree
def preordertraverse(p): #recursion

	if (p == None):
		return 
	else:
		print(p.data,end=' ')
		preordertraverse(p.left)
		preordertraverse(p.right)


# Driver code for prefix
a = "*+ab-cd"
s,a=prefix_to_tree(a)
print("The Infix expression is:")
inordertraverse(s)
print()
print("The Postfix expression is:")
postordertraverse(s)
print()
print("prefix traverse will give us the same expression: ")
print(preordertraverse(s))
# Driver code for infix
print("\n")
postfix = 'ab+cde+**'
root = postfix_to_tree(postfix)
print('Postfix Expression: ', end='')
postordertraverse(root)
print('\nInfix Expression: ', end='')
inordertraverse(root)

