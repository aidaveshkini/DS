

class Node: #✅
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # Check if the stack is empty or not
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def Top(self):

        if self.isEmpty():
            raise Exception("your stack is empty")
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Remove a value from the stack.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
        # Get the current size of the stack
    def getSize(self):
        return self.size
    def print(self):
        cur = self.head.next
        out = ""
        while cur:
            out = out + cur.value + " "
            cur = cur.next
        return out[:-2]

def is_operator(char):   #checks if the character is a binary operator✅
	if (char =='+' or char =='-' or char =='*' or char =='/' or char == '^'):
		return True
	return False

def preced(operator): #define the precedence of the operators✅
    if (operator == "+" or operator == "-"):
        return 1
    if (operator == "*" or operator == "/"):
        return 2
    if (operator == "^"):
        return 3

def reverse(expr):   ##get an expression as argument & Reverse it✅
    x = expr[::-1]
    rev_expr =""
    for c in x:
        if c == "(":
            rev_expr = rev_expr + ")"
        elif c == ")":
            rev_expr = rev_expr + "("
        else:
            rev_expr = rev_expr + "%s"%(c)
    return rev_expr


    
def infix_to_postfix(expr): #convert infix expression to postfix expression
    postfix = ""
    s = Stack()
    for c in expr:  #itrate the expression string
        if c == "(":  # open parenthesis 
            s.push("(")
            print(s.isEmpty())
            print(s.print())
          
        elif c == "^":
            s.push("^")
  
        elif is_operator(c):
            if s.isEmpty():
                s.push(c)
               
            elif s.Top()== "(":
                s.push(c)

            else:   # s.top is an operator too
                while not (s.isEmpty()) and preced(s.Top()) >= preced(c):
                    postfix = postfix + "%s"%(s.Top())
                    s.pop()
                    if not s.isEmpty() and s.Top() == "(":
                        s.pop()  
                        break

                s.push(c)


        elif c == ")": # close parenthesis
            while s.Top() != "(" and not s.isEmpty():
                postfix = postfix + "%s"%(s.Top())
                s.pop()
            s.pop()


        else:   #if the c is an operand
            postfix = postfix + "%s"%(c)

    while not s.isEmpty(): #when itrating the infix expression ends,
                           #insert all the remainig operators in the stack after the postfix expression
        postfix = postfix + "%s"%(s.Top())
        s.pop()
        
    return postfix



def infix_to_prefix(expr):
    rev = reverse(expr)
    postfix = infix_to_postfix(rev)
    prefix = reverse(postfix)
    return prefix

print(infix_to_prefix("a+b-(c^d)"))

