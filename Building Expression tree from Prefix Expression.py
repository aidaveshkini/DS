# Python3 program to construct an expression tree
# from prefix expression

# Represents a node of the required tree
class node:
	def __init__(self,c):
		self.data=c
		self.left=self.right=None

# Function to recursively build the expression tree
def pstfix_to_tree(a):

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
		p.left,q=pstfix_to_tree(a[1:])
		# Build the right sub-tree
		p.right,q=pstfix_to_tree(q)
		return p,q
		

# Function to print the infix expression for the tree
def infixtraverse(p): #recursion

	if (p == None):
		return
	else:
		infixtraverse(p.left)
		print(p.data,end=' ')
		infixtraverse(p.right)

# Function to print the postfix expression for the tree
def posttraverse(p):

	if (p == None):
		return
	else:
		posttraverse(p.left)
		posttraverse(p.right)
		print(p.data,end=' ')

def prefixtraverse(p):

	if (p == None):
		return 
	else:
		print(p.data,end=' ')
		prefixtraverse(p.left)
		prefixtraverse(p.right)


# Driver code
if __name__ == '__main__':
	
	a = "*+ab-cd"
	s,a=pstfix_to_tree(a)
	print("The Infix expression is:")
	infixtraverse(s)
	print()
	print("The Postfix expression is:")
	posttraverse(s)
	print()
	print("prefix traverse will give us the same expression: ")
	print(prefixtraverse(s))

