# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):  # loop from 2 to n
            result *= i
        return result

# Sample call
num = int(input("Please provide a number to find it's factorial: "))
print(f"Factorial of {num} is:", factorial(num))
