a = 10
a1 = a // 2
a2 = a % 2
if a2 == True:
    a1 += 1

b = 20
b1 = b // 2
b2 = b % 2
if b2 == True:
    b1 += 1

c = 11
c1 = c // 2
c2 = c % 2
if c2 == True:
    c1 += 1


d = c1 + b1 + a1
print(d)