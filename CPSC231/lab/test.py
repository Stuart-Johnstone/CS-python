a = 12
def mirrorBits(a):
    a = bin(a)[2:]
    print(a)
    n = ""

    for i in range(len(a)-1,0,-1):
        n += a[i]
    print(n)
    a = "0b" + a
    return int(a,0)
print(mirrorBits(a))