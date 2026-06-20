# Program to swap two variables using tuple unpacking
# This is the Pythonic way to swap without needing a temporary variable

# Initialize variables with values
x = 10
y = 20

# Swap using tuple unpacking (simultaneous assignment)
x, y = y, x

# Display swapped values
print("after swaping:")
print(f"x = {x}, y = {y}")