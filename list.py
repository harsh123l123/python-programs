# Program to perform various operations on lists
# Operations: sum, product, maximum, and minimum

# Define two sample lists
list1 = [1, 3, 6, 9, 7, 5, 7, 7]
list2 = [3, 6, 9, 5, 8, 3, 6, 9]

# Calculate and display sum of list1
total_sum = sum(list1)
print("sum of list1 is :", total_sum)

# Calculate and display product of list1
product = 1
for i in list1:
   product *= i
print("product of list1 is :", product)

# Find and display largest element in list1
largest = max(list1)
print("largest element in list1 is :", largest)

# Find and display smallest element in list1
minimum = min(list1)
print("smallest element in list1 is :", minimum)