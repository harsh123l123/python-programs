# Program to swap two variables using tuple unpacking
# This is the Pythonic way to swap without needing a temporary variable

# Initialize variables with values
a = 10
b = 20

# Swap using tuple unpacking (simultaneous assignment)
a, b = b, a

# Display swapped values
print("after swaping:")
print(f"a = {a}, b = {b}")