
# class of stack node
class Node:
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

    #print all elements in the stack🟥
    def print(self):
        cur = self.head.next
        out = ""
        while cur:
            out = out + cur.value + " "
            cur = cur.next
        return out[:-2]



#checks if the character is a binary operator
def is_operator(char):   
	if (char =='+' or char =='-' or char =='*' or char =='/' or char == '^'):
		return True
	return False

#define the precedence of the operators
def preced(operator): 
    if (operator == "+" or operator == "-"):
        return 1
    if (operator == "*" or operator == "/"):
        return 2
    if (operator == "^"):
        return 3

#get an expression as argument & Reverse it
def reverse(expr):   
    x = expr[::-1]           #reverse by slicing
    rev_expr =""
    for c in x:
        if c == "(":         #also reverse the parantheses
            rev_expr = rev_expr + ")"
        elif c == ")":
            rev_expr = rev_expr + "("
        else:
            rev_expr = rev_expr + "%s"%(c)
    return rev_expr


#convert infix expression to postfix expression    
def infix_to_postfix(expr): 
    postfix = ""
    s = Stack()               #creat an empty stack to store operators & paranthesis
    for c in expr:           
        if c == "(":          #for the caracters:open parenthesis :
            s.push("(")       
          
        elif c == "^":        #for the caracters:power :
            s.push("^")       
  
        elif is_operator(c):  #for the caracters:operators :
            if s.isEmpty():       #if caracter:operator & stack:empty
                s.push(c)         
               
            elif s.Top()== "(":   #if caracter:operator & stack.top: (
                s.push(c)

            else:                 #if both character & s.top are operators
                                  #while stack.top is precedent:
                while not (s.isEmpty()) and preced(s.Top()) >= preced(c):
                    postfix = postfix + "%s"%(s.Top())   #add stack.top into postfix string
                    s.pop()                              #delete s.top
                    if not s.isEmpty() and s.Top() == "(":    #but if next s.top is ( ,
                        s.pop()                               #delete the ( from stack,
                        break                                 #& end the adding into postfix expr,
                                                              #& push the c:operator in stack
                s.push(c)


        elif c == ")":         #for the characters:close parenthesis:
            while s.Top() != "(" and not s.isEmpty():  #until reaching ( ,
                postfix = postfix + "%s"%(s.Top())     #add the stack operators into postfix str
                s.pop()                                #delete the added operators
            s.pop()                                    #then add the c:operator


        else:                 #for the characters:operand:
            postfix = postfix + "%s"%(c)   #add them into postfix string

    while not s.isEmpty(): #when itrating the infix expression ends,
                           #insert all the remainig operators in the stack after the postfix expression
        postfix = postfix + "%s"%(s.Top())
        s.pop()
        
    return postfix


#convert infix expression to prefix expression    
def infix_to_prefix(expr):
    rev = reverse(expr)    #first reverse the infix expr
    postfix = infix_to_postfix(rev)   #convert the reversed expr to postfix
    prefix = reverse(postfix)         #again reverse the postfix expr to get prefix one
    return prefix


expr = "a+b-(c^d)"
print("the infix expression is:  %s"%(expr))
print("if we reverse it:", end="  ")
print (reverse(expr))
print("convert to postfix:",end="  ")
print(infix_to_postfix(reverse(expr)))
print("reverse it again:",end="  ")
print(infix_to_prefix(expr))

