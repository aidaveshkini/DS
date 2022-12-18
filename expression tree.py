from collections import deque

# Represents a node of the required tree✅
class ExprssionTree_node:
	def __init__(self,data=None):
		self.parent=None
		self.data=data
		self.left=self.right=None

class Expression_Tree:
	def __init__(self):
		self.root = None

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
			subtree1 = Expression_Tree()
			subtree1.root= self.root.left
			subtree2 = Expression_Tree()
			subtree2.root= self.root.right
			subtree1.preordertraverse()
			subtree2.preordertraverse()

# Function to build the expression tree from a given prefix expression
def prefix_to_tree(a): #recursion

	# If its the end of the expression
	if (a == ''):
		return ''

	# If the character is an operand
	if a[0]>='a' and a[0]<='z':
		return ExprssionTree_node(a[0]),a[1:]
	else:
		# Create a node with a[0] as the data and
		# both the children set to null
		p=ExprssionTree_node(a[0])
		# Build the left sub-tree
		p.left,q=prefix_to_tree(a[1:])
		# Build the right sub-tree
		p.right,q=prefix_to_tree(q)
		return p,q

# Function to build the expression tree from a given postfix expression
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
	tree.root = s.pop()
	return tree

# Function to build the expression tree from a given infix expression with complete parantesis✅
def parInfixExpr_to_tree(expr):
	#first we create an empty-labeled node
	node = ExprssionTree_node('empty')
	#we iterate the string of expression & make the appropriate node for each character:
	for c in expr:
		if is_operator(c):
			node.data = c
			#each operator has 1 or 2 operand(s) & is located befor or between them(operands)
			#so after an operator in string,we meet the right-side operand
			next_node = ExprssionTree_node('empty')
			node.right = next_node
			next_node.parent = node
			node = node.right
		elif (c == '('):
			#open parentesis means priority & prior expression goes deeper
			next_node = ExprssionTree_node('empty')
			node.left= next_node
			next_node.parent = node
			node = node.left
		elif (c == ')'):
			#close paremtesis means prior expression ends so we go up
			if(node.parent):
				node = node.parent
		else: #is operand
			node.data = c
			#each operand in expression is located befor or after an operator
			#so either its the right-side or left-side operand we go back to its parent node in tree & continue iterating
			#go to the parent
			node = node.parent
	while (node.parent):
		node = node.parent
	your_tree = Expression_Tree()
	your_tree.root = node
	return your_tree

def infix_to_tree(expr):
	pass

def is_operator(char):   #checks if the character is a binary operator✅
	if (char =='+' or char =='-' or char =='*' or char =='/' or char =='^'):
		return True
	return False

def infix_to_prefix(expr):
	tree = infix_to_tree(expr)
	tree.preordertraverse()




#driver code for postfix expression to tree & its traverses:✅
print('postfix expression is:  ab+cde+**')
tree = postfix_to_tree('ab+cde+**')
print('the postfix expression is: ')
tree.postordertraverse()
print('\n the prefix expression is:')
tree.preordertraverse()
print('\n\n')

#driver code for prefix expression to tree & its traverses:
tupleee = prefix_to_tree('*+ab-cd')
print('the postfix expression is: ')
tree = Expression_Tree()
tree.root = tupleee[0]
tree.postordertraverse()
print('\n the prefix expression is:')
tree.preordertraverse()
print('\n\n')


#driver code for infix expression with complete parantesis to tree & its traverses:✅
print('parinfix expression is:  (3+((5+9)*2)')
tree = parInfixExpr_to_tree('(3+((5+9)*2)')
print('the postfix expression is:  ')
tree.postordertraverse()
print('\n the prefix expression is:  ')
tree.preordertraverse()
print('\n\n')


#driver code for infix expression to tree & its traverses:🟥
#print('infix expression is:  3+(5+9)*2')
#tree = infix_to_tree('3+(5+9)*2')
#print('the postfix expression is:  ')
#tree.postordertraverse()
#print('\n the prefix expression is:  ')
#tree.preordertraverse()
#print('\n\n')

#driver code for infix to prefix:🟥
#infix_to_prefix(3+(5+9)*2)
