from collections import deque

# Represents a node of the required tree✅
class ExprssionTree_node:
	def __init__(self,data):
		self.data=data
		self.left=self.right=None
class Expression_Tree:
    def __init__(self):
        self.root = None

<<<<<<< HEAD
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
=======

    def is_binaryOpr(self,char):
        if (char == '+' or char == '-' or char == '*' or char == '/' or char == '^'):
            return True
        return False

    def is_unaryOpr(self,char):
        if (char == 'sin' or char == 'log'):
            return True
        return False

    def is_operator(self,char):
        if (self.is_binaryOpr(char) or self.is_unaryOpr(char)):
            return True
        return False

    def preorder_trav(self):
        node = self.root
        if node:
            print(node.data,end=' ')
            node.left_child.preorder_trav
            node.right_child.preorder_trav
        return
    def inorder_trav(self):
        node = self.root
        if node:
            node.left_child.inorder_trav()
            print(node.data,end=' ')
            node.right_child.inorder_trav()
        return
    def postorder_trav(self):
        node = self.root
        if node:
            node.left_child.postorder_trav()
            node.right_child.postorder_trav()
            print(node.data,end=' ')
        return

>>>>>>> d865c919c7d09e0b412a2fa1f973a89be4d7886a





<<<<<<< HEAD
tree = prefix



#tree = postfix_to_tree('ab+')
#tree.postordertraverse()
=======
bitree = Expression_Tree()
while True:
    print('1: prefixExp to tree\n2: parinfixExp to tree\n3: infixExp to tree\n4: postfixExp to tree')
    print('5: Traverse Preorder\n6: Travers Inorder\n7: Traverse Postorder\n 8: exit\n')
    select = int(input("choose a number: "))
    if (select == 2):
        parinfixExpr = str(input('enter your infix expression: '))
        bitree.parInfixExpr_to_tree(parinfixExpr)
    elif (select == 5):
        bitree.preorder_trav()
    elif (select == 6):
        bitree.inorder_trav
    elif (select == 7):
        bitree.postorder_trav
    elif (select == 8):
        print("    finished;)")
        break
>>>>>>> d865c919c7d09e0b412a2fa1f973a89be4d7886a


# (3+((5+9)*2)