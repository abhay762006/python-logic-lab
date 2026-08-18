user = input("Enter a number: ")

temp = int(user)
reverse = 0

for digit in range(len(user)):
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if int(user) == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")