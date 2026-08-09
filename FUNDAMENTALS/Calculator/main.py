
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


def calculate(n1, n2):
    print('+')
    print('-')
    print('*')
    print('/')
    op = input("Select the operation\n")
    if op == '+':
        print(add(n1,n2))
    elif op == '-':
        print(subtract(n1,n2))
    elif op == '*':
        print(multiply(n1,n2))
    elif op == '/':
        print(divide(n1,n2))
    else:
        print('Invalid operation')
print('Welcome to the Calculator')
while True:
    k = input("Do you want to calculate a number?(y/n)\n")
    if k == 'y':
        n1 = float(input("Enter a first number\n"))
        n2 = float(input("Enter second number\n"))

        calculate(n1,n2)
    else:
        break


