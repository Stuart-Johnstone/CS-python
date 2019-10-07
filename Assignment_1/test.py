a = input("give numbers ")#1
while a.isdigit() != True:
    a = input("give numbers ")#1
b = input("give numbers ")
while b == 0 or b.isdigit() != True:
    b = input("give numbers ")
a = int(a)
b = int(b)
if str(a)[-1] in [0,2,4,6,8]:
    print("even")
else:
    print("odd")


print(int(a)/int(b))#2

x = 0#3
b = 0
while x <=(a**0.5):
    x += 1
    while b <= x:
        if b *x == a:
            break
        else:
            b +=1
    if b * x == a:
        print("not prime")
        break
if x > a**0.5:
    print("prime")

lst = [0,1]
while lst[-1] < 100:
    lst.append(lst[-1]+lst[-2])
print(lst)
