# Program to swap two variables using a temporary variable
# Traditional method of swapping variables

# Input two numbers from user
a = int(input("enter first number : "))
b = int(input("enter second number : "))

# Swap using temporary variable
c = a      # Store first number in temporary variable
a = b      # Assign second number to first
b = c      # Assign temporary value (original first) to second

# Display the swapped values
print("After swapping:")
print("First number:", a)
print("Second number:", b)