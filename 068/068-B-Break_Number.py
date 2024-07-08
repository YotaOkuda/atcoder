'''N = int(input())
a = [1, 2, 4, 8, 16, 32, 64]
b = 0
for i in a:
    if N >= i:
        b = i
    else:
        break
print(b)'''

#別解　2をNが超えるまでかける，1回余分にかけてるから最後に割る
'''N = int(input())
i = 1
while i <= N:
    i *= 2
i /= 2
print(int(i))'''

#別解　全探索
n = int(input())

max_count = 0
max_value = 1

for i in range(1, n+1, 1):
    count = 0
    t = i

    while t > 0:
        if t%2 == 0:
            t = t//2
            count += 1
        else:
            break

    if max_count < count:
        max_count = count
        max_value = i

print(max_value)