# Program to generate the Fibonacci sequence
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
# Each number is the sum of the two preceding ones

# Input the number of terms to generate
n = int(input("enter number of terms: "))

# Initialize empty list and first two Fibonacci numbers
fib = []
a, b = 0, 1

# Generate Fibonacci sequence
for i in range(n):
    fib.append(a)  # Add current number to list
    a, b = b, a + b  # Update a and b to next pair

# Display the Fibonacci sequence
print("Fibonacci sequence:")
print(fib)
