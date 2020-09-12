num = int(input("enter somthing"))
base = int(input("enter a base"))
b = bin(num)[2:]
o = oct(num)[2:]
h = hex(num)[2:]
print(b,o,h)
x = num
lst = []
while x >0:
    lst.append(int(x%base))
    xmod = x%base
    x = (x-xmod)/base
lst.reverse()
print(lst)

x = 0
for i in range(len(lst)):
    if lst[i] != 0:
        x += base ** (len(lst)-i-1)

print(x)
        

