# Python3 program to construct an expression tree
# from prefix expression

# Represents a node of the required tree
class node:
	def __init__(self,c):
		self.data=c
		self.left=self.right=None

# Function to recursively build the expression tree
def add(a):

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
		p.left,q=add(a[1:])
		# Build the right sub-tree
		p.right,q=add(q)
		return p,q
		

# Function to print the infix expression for the tree
def inr(p): #recursion

	if (p == None):
		return
	else:
		inr(p.left)
		print(p.data,end=' ')
		inr(p.right)

# Function to print the postfix expression for the tree
def postr(p):

	if (p == None):
		return
	else:
		postr(p.left)
		postr(p.right)
		print(p.data,end=' ')

# Driver code
if __name__ == '__main__':
	
	a = "*+ab-cd"
	s,a=add(a)
	print("The Infix expression is:")
	inr(s)
	print()
	print("The Postfix expression is:")
	postr(s)

# This code is contributed by Amartya Ghosh
