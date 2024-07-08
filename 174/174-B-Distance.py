import math as m
n, d = map(int, input().split())

X = []
count = 0

for i in range(n):
    x, y = map(int, input().split())
    distance = m.sqrt(x**2 + y**2)
    X.append(distance)

for j in X:
    if j <= d:
        count += 1

print(count)