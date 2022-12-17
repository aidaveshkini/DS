
class ExpressionTree_node:
    def __init__(self,data=None):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None
class Expression_Tree:
    def __init__(self):
        self.root = None
    def parInfixExpr_to_tree(self,infixExpr):
        #we want to make a tree of an infix expression with complete parenthesis
        #we begin with the first null node:🟥
        #we iterate the string of expression & make the appropriate node for each character:
        node = ExpressionTree_node()
        for i in range (len(infixExpr)):
            if self.is_operator(infixExpr[i]):
                node.data = infixExpr[i]
                #each operator has 1 or 2 operand(s) & is located befor or between them(operands)
                #so after an operator in string,we meet the right-side operand
                next_node = ExpressionTree_node()
                node.right_child = next_node
                next_node.parent = node
                node = node.right_child
            elif (infixExpr[i] == '('):
                #open parentesis means priority & prior expression goes deeper
                next_node = ExpressionTree_node()
                node.left_child = next_node
                next_node.parent = node
                node = node.left_child
            elif (infixExpr[i] == ')'):
                #close paremtesis means prior expression ends so we go up
                node = node.parent
            else: #is operand
                node.data = infixExpr[i]
                #each operand in expression is located befor or after an operator
                #so either its the right-side or left-side operand we go back to its parent node in tree & continue iterating
                if (not node.parent):
                #make a null parent node
                  next_node = ExpressionTree_node()
                  node.parent = next_node
                  next_node.left_child = node
                #go to the parent
                node = node.parent
        while (node.parent):
            node = node.parent
        self.root = node
        print("your expression tree is built:)\n")


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




#driver code for infixExpr to tree
bitree2 = Expression_Tree()
bitree2.parInfixExpr_to_tree("(3+((5+9)*2)")
bitree2.inorder_trav()


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


# (3+((5+9)*2)