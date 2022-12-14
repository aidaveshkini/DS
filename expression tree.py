
class ExpressionTree_node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None
class Expression_Tree:
    def __init__(self):
        self.root = None

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



bitree = Expression_Tree()
print('1: prefixExp to tree\n2: parinfixExp to tree\n3: infixExp to tree\n4: postfixExp to tree\n5: Traverse Preorder\n6: Travers Inorder\n7: Traverse Postorder\n 8: exit')
select = int(input("choose a number: "))
if (select == 5):
    bitree.preorder_trav()
elif (select == 6):
    bitree.inorder_trav
elif (select == 7):
    bitree.postorder_trav
