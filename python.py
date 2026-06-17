# Program to demonstrate conditional logic and truth values
# Tests logical operators (or, and, not) and ternary operator

# Initialize variables with different data types
x = 15  # Non-zero integer (truthy)
y = 0   # Zero integer (falsy)
z = ""  # Empty string (falsy)

# Test logical conditions
if x or y or z:  # True if any value is truthy
    print("A")
elif not x and not y:  # True if both x and y are falsy
    print("B")
elif x > 10:  # True if x is greater than 10
    print("C")
else:
    print("D")

# Ternary operator: return "Yes" if condition is true, else "No"
result = "Yes" if x > 10 and not z else "No"
print(result)