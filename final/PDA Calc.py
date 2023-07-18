import math

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False
Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators
valid_list=['+', '-', '*', '/', '(', ')', '^','tan','cos','sin','abs','ln','exp','sqrt']
func_list=['tan','cos','sin','abs','ln','exp','sqrt']
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators
 
 
def infixToPostfix(expression): 

    stack = [] # initialization of empty stack

    output = '' 

    for character in expression:
        #print(character)
        if character in valid_list or is_float(character):

            if is_float(character):  # if an operand append in postfix expression
                output+= character+" "

            elif character=='(':  # else Operators push onto stack
                stack.append('(')

            elif character==')':
                while stack and stack[-1]!= '(':
                    output+=stack.pop()+" "
                stack.pop()

            elif character in func_list :
                while stack and stack[-1]!='(' :
                    output+=stack.pop()+" "
                stack.append(character)

            else: 
                while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:
                    output+=stack.pop()+" "
                stack.append(character)
        else:
            print("INVALID")
            exit()  

    while stack:

        output+=stack.pop()+" "
    return output


def evaluatePostfix(exp):
    myStack = []
    for i in exp :
        # print(myStack)
        if is_float(i):
            myStack.append(i)
        elif i=="tan":
                val1 = myStack.pop()
                myStack.append(str(math.tan(float(val1))))

        elif i=="sin":
                val1 = myStack.pop()
                myStack.append(str(math.sin(float(val1))))


        elif i=="cos":
                val1 = myStack.pop()
                myStack.append(str(math.cos(float(val1))))

        elif i=="abs":
                val1 = myStack.pop()
                myStack.append(str(math.abs(float(val1))))


        elif i=="exp":
                val1 = myStack.pop()
                myStack.append(str(math.exp(float(val1))))

        elif i=="ln":
                val1 = myStack.pop()
                if float(val1) < 0 :
                    print("INVALID")
                    exit()
                else:
                    myStack.append(str(math.tan(float(val1))))
        else:
            val1 = myStack.pop()
            val2 = myStack.pop()
            if i=="+":
                myStack.append(str(float(val2)  +  float(val1))) 
            if i=="-":
                myStack.append(str(float(val2)  -  float(val1)))
            if i=="*":
                myStack.append(str(float(val2)  *  float(val1))) 
            if i=="/":
                myStack.append(str(float(val2)  /  float(val1)))
            if i=="^":
                myStack.append(str(float(val2)  **  float(val1)))                   
        
    return float(myStack.pop())

expression = input()

left_p=0
right_p=0
for i in expression:
    if i == "(":
        left_p +=1
for i in expression:
    if i == ")":
        right_p +=1


for i in range(len(expression)-2):
    if expression[0] in Operators:
        if expression[0]==')' or expression[0]==')':
            continue
        print("INVALID")
        exit()  

    elif expression[i].isdigit() and expression[i+1]==" " and expression[i+2].isdigit() :
        print("INVALID")
        exit()

if left_p != right_p:
    print("INVALID")
else :
    expression=expression.replace("("," ( ")
    expression=expression.replace(")"," ) ")
    expression=expression.replace("  "," ")
    result = expression.split(" ")
    result = list(filter(None, result))
    #print(result)
    # print(infixToPostfix(result))
    try :
        exp=infixToPostfix(result).split(" ")
        exp = list(filter(None, exp))
        #print(exp)
        answer=evaluatePostfix(exp)
        format_float = "{:.2f}".format(answer)
        print(format_float)
    except:
        print("INVALID")



