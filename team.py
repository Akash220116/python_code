n = 0
i = 0
j = 0
m = 0
sum = 0
count = 0

n = int(input())

if n >= 1 and n <= 1000:
    for i in range(0, n):
        for j in range(0, 3):
            m = int(input())
            sum = sum + m
        if sum >= 2:
            count = count + 1
        sum = 0

    print(count)
