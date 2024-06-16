# Create a python program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

# Input numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers and print the result
if num1 > num2:
    print(f"The first number ({num1}) is greater than the second number ({num2}).")
elif num1 < num2:
    print(f"The first number ({num1}) is less than the second number ({num2}).")
else:
    print(f"The first number ({num1}) is equal to the second number ({num2}).")