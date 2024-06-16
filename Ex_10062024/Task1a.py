# One Develop Python script that calculates the square and cube of a given number.
# Input number from the user
num = float(input("Enter a number: "))

# Calculate Square and Cube of the number
square = num ** 2
cube = num ** 3

# Print the results
print(f"Number: {num}")
print(f"Square: {square}")
print(f"Cube: {cube}")


# One Develop a one line Python script that calculates the square and cube of a given number.
print("Square:", (num := float(input("Enter a number: ")))**2, "Cube:", num**3)