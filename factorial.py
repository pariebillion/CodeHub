def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial cannot be calculated for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    result = factorial(number)
    print("The factorial of", number, "is", result)
