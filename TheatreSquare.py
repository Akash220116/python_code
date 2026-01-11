m = 0
n = 0
a = 0
sum = 0
sum1 = 0
r = 0
r1 = 0
d = 0
d1 = 0
s = 0
s1 = 0
flag = 0

m = int(input())
n = int(input())
a = int(input())

if n >= 1 and a <= 1000000000:
    r = m % a
    if r > 0:
        s = 1
    d = m // a
    sum = d + s

    r1 = n % a
    if r1 > 0:
        s1 = 1
    d1 = n // a
    sum1 = d1 + s1

    flag = sum * sum1
    print(flag)
