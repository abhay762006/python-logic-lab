user = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, user + 1):
    factorial *= i
print(f"The factorial of {user} is {factorial}.")
