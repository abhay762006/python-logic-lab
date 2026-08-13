def is_prime(num):
    num = int(input("Enter the number: "))

    if num == 2 or num == 3 or num == 5 or num == 7:
        print("prime")
    elif num % 2 == 0:
        print("not prime")
    elif num % 3 == 0:
        print("not prime")
    elif num % 5 == 0:
        print("not prime")
    elif num % 7 == 0:
        print("not prime")
    else:
        print("prime")

is_prime(num)