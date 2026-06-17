# Program to determine if a year is a leap year
# Rules for leap year:
# - Divisible by 400: leap year
# - Divisible by 100: not a leap year
# - Divisible by 4: leap year
# - Otherwise: not a leap year

# Input year from user
year = int(input("enter year :"))

# Check leap year conditions
if year % 4 == 0:
  if year % 400 == 0:
     print("leap year ")
  elif year % 100 == 0:
      print("not a leap year")
  else:
     print("leap year")    
else:
  print("not a leap year")