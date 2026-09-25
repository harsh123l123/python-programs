import re 

s = input()
m = re.search(r"([a-zA-z0-9])\1",s)
if m:
    print(m.group(1))
else:
    print("no match")    
