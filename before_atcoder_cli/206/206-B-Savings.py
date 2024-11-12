N = int(input())

'''total = 0
count = 0
for i in range(1, N+1):
    total += i
    count += 1
    if total >= N:
        print(count)
        break'''

#別解
total = 0
count = 0
while total < N:
    count += 1
    total += count

print(count)