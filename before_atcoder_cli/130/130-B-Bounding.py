n, x = map(int, input().split())
L = list(map(int, input().split()))

sum = 0
count = 1
for l in L:
    sum += l
    if sum > x:
        break
    count += 1

print(count)