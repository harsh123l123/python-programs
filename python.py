x = 15
y = 0
z = ""

if x or y or z:
    print("A")
elif not x and not y:
    print("B")
elif x > 10:
    print("C")
else:
    print("D")

result = "Yes" if x > 10 and not z else "No"
print(result)