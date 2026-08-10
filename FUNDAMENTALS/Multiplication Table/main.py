user = int(input("Enter a number to generate its multiplication table: "))
for i in range(1, 11):
    result = user * i
    print(f"{user} x {i} = {result}")