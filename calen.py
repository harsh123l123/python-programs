# Program to display a calendar for a given month and year
# Uses the built-in calendar module

import calendar

# Input year and month from user
year = int(input("enter year: "))
month = int(input("enter month:"))

# Display the calendar for the specified month and year
print(calendar.month(year, month))