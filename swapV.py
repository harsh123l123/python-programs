# Program to swap two variables using a temporary variable
# Traditional method of swapping variables

# Input two numbers from user
x = int(input("enter first number : "))
y = int(input("enter second number : "))

# Swap using temporary variable
z = x      # Store first number in temporary variable
x = y      # Assign second number to first
y = z      # Assign temporary value (original first) to second

# Display the swapped values
print("After swapping:")
print("First number:", x)
print("Second number:", y)