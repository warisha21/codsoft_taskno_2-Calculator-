# Addition
def add(x,y):
    return x + y

# Suubtraction
def sub(x,y):
    return x - y

# Multiplication
def mul(x,y):
    return x * y

# Division
def div(x,y):
    return x / y

def power(x,y):
    return x ** y

# Enter inputs
inp1 = int(input(print("Enter input 1")))
inp2 = int(input(print("Enter input 2")))

# Choose Mathematical operation
inp_op = input( print("Select the mathematical operator :+ for Addition - fro Subtraction * for Multiplication / for division ^ for power"))

if inp_op == '+':
    print (f"The sum of {inp1} + {inp2} = {add(inp1,inp2)}")

if inp_op == '-':
    print (f"The difference of {inp1} - {inp2} = {sub(inp1,inp2)}")

if inp_op == '*':
    print (f"The product of {inp1} * {inp2} = {mul(inp1,inp2)}")

if inp_op == '/':
    print (f"The quotient of {inp1} / {inp2} = {div(inp1,inp2)}")

if inp_op == '^':
    print(f"The {inp1} ^ {inp2}  = {power(inp1,inp2)}")

