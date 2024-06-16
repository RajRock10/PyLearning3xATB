# Task - Fibonacci series
# Write a python program to print Fibonacci series of a given number.
# 0,0+1, 0+1+1,
# For example :-
# n = 7
# 0, 1, 2, 3, 5, 8, 13

# Input the number of terms from the user
num_of_terms = int(input("Enter the number of terms: "))

# Initialize the first two terms of the Fibonacci series
a, b = 0, 1

# Generate and print the Fibonacci series
print("Fibonacci series:")
for _ in range(num_of_terms):
    print(a, end=" ")
    a, b = b, a + b