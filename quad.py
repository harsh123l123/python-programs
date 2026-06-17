# Program to solve quadratic equations (ax^2 + bx + c = 0)
# Uses the quadratic formula and discriminant to find roots
# Formula: x = (-b ± √(b² - 4ac)) / 2a

import math

# Input coefficients from user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate discriminant (b² - 4ac)
# Discriminant determines the nature of roots
discriminant = b**2 - 4*a*c

# Case 1: Two real roots (discriminant > 0)
if discriminant > 0:
  root1 = (-b + math.sqrt(discriminant)) / (2*a)
  root2 = (-b - math.sqrt(discriminant)) / (2*a)
  print(f"Root 1: {root1}")
  print(f"Root 2: {root2}")      
# Case 2: One real root (discriminant = 0)
elif discriminant == 0:
  root = -b / (2*a)
  print(f"Root: {root}")
# Case 3: Complex roots (discriminant < 0)
else:
  real_part = -b / (2*a)
  imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
  print(f"Root 1: {real_part} + {imaginary_part}i")
  print(f"Root 2: {real_part} - {imaginary_part}i")
