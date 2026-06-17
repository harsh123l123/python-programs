# Program to check if a number is positive, negative, or zero

# Input a number from user
a = float(input("enter a number :"))

# Check if the number is positive, negative, or zero
if a > 0:
    print("the number is positive")
elif a < 0:
    print("the number is negative")
else:
    # If not positive and not negative, it must be zero
    print("the number is zero") 