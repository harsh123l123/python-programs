# Program to calculate the factorial of a number
# Factorial of n (n!) = n * (n-1) * (n-2) * ... * 1

# Input number from user
num = int(input("enter number : "))

# Initialize factorial result and loop counter
fact = 1
i = 1

# Multiply all numbers from 1 to num
while i <= num:
  fact = fact * i
  i = i + 1

# Display the factorial result
print("factorial is :", fact)
