# Program to check if a number is prime
# A prime number is divisible only by 1 and itself
# Numbers less than 2 are not prime

# Input number from user
num = int(input("enter number : "))

# Check if number is less than 2 (not prime)
if num < 2:
  print("not prime")
else:
  # Check divisibility from 2 to num-1
  for i in range(2, num):
    if num % i == 0:
       # If divisible by any number, it's not prime
       print("not prime")
       break
    else:
      # If no divisor found, number is prime
      print("prime")
      break


