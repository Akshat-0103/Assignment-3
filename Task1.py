# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample number
number = 5

# Call the function and display the result
print("The factorial of", number, "is:", factorial(number))
