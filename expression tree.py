
class ExpressionTree_node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None
class Expression_Tree:
    def __init__(self):
        self.root = None
    def parInfixExpr_to_tree(self,infixExpr):
        #we want to make a tree of an infix expression with complete parenthesis
        #we begin with the first null node:
        node = self.root
        #we iterate the string of expression & make the appropriate node for each character:
        for i in range (len(infixExpr)):
            if self.is_operator(infixExpr[i]):
                node.data = infixExpr[i]
                #each operator has 1 or 2 operand(s) & is located befor or between them(operands)
                #so after an operator in string,we meet the right-side operand
                #so:
                node = node.right_child
            elif (infixExpr[i] == '('):
                #
                node = node.right_child
            elif (infixExpr[i] == ')'):
                #
                node = node.left_child
            else: #is operand
                node.data = infixExpr[i]
                #each operand in expression is located befor or after an operator
                #so either its the right-side or left-side operand we should go back to its parent node in tree & continue iteration
                node = node.parent

        print("your expression tree is built:)")

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
            print(node.data)
            node.left_child.preorder_trav
            node.right_child.preorder_trav
        return
    def inorder_trav(self):
        node = self.root
        if node:
            node.left_child.inorder_trav
            print(node.data)
            node.right_child.inorder_trav
        return
    def postorder_trav(self):
        node = self.root
        if node:
            node.left_child.postorder_trav
            node.right_child.postorder_trav
            print(node.data)
        return



class stack:
   def __init__(self):
      self.arr = []
   def push(self, data):
      self.arr.append(data)
   def pop(self):
      try:
         return self.arr.pop(-1)
      except:
         pass
   def top(self):
      try:
         return self.arr[-1]
      except:
         pass
   def size(self):
      return len(self.arr)


def postfix_to_tree(a):
    nodes_stack = stack()
    for i in range (len(a)):
        # If the character is an operand
        if a[i]>='a' and a[i]<='z':
            nodes_stack.push(a[i])
        else:
            right = nodes_stack.pop()
            left = nodes_stack.pop()
            new_node = ExpressionTree_node(a[i])
            new_node.left_child = left
            new_node.right_child = right
            nodes_stack.push(new_node)
    TREE = Expression_Tree()
    TREE.root = nodes_stack.pop()
    return TREE


bitree = Expression_Tree()
print('1: prefixExp to tree\n2: parinfixExp to tree\n3: infixExp to tree\n4: postfixExp to tree\n5: Traverse Preorder\n6: Travers Inorder\n7: Traverse Postorder\n 8: exit')
select = int(input("choose a number: "))
if (select == 1):
    prefixExpr = input('enter your prefix expression: ')
    p = prefix_to_tree(prefixExpr)
    inr(p)
elif (select == 2):
    infixExpr = input('enter your infix expression: ')
    bitree.parInfixExpr_to_tree(infixExpr)
elif (select == 4):
    postfixExpr = input('enter your postfix expression: ')
    postfix_to_tree(postfixExpr).postorder_trav()
elif (select == 5):
    bitree.preorder_trav()
elif (select == 6):
    bitree.inorder_trav
elif (select == 7):
    bitree.postorder_trav

# 3+((5+9)*2)