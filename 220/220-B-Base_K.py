k = int(input())
a, b = list(map(str, input().split()))

total_a, total_b = (0, 0)
index_a = 0
index_b = 0
for i in range(len(a) - 1, -1, -1):
    total_a += int(a[i])*(k**index_a)
    index_a += 1

for c in range(len(b) - 1, -1, -1):
    total_b += int(b[c])*(k**index_b)
    index_b += 1

print(total_a*total_b)