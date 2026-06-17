# Program to display day name based on day number
# Uses match-case statement (Python 3.10+)
# Day numbers: 1=Monday, 2=Tuesday, ..., 7=Sunday

# Input day number from user
n = int(input("enter a day:"))

# Match day number to day name
match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:  # Default case for invalid input
        print("Invalid day")

        