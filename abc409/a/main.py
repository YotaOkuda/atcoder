N = int(input())
T = str(input())
A = str(input())

ans = False
for i in range(N):
    count = 0
    if T[i] == 'o':
        count += 1
    if A[i] == 'o':
        count += 1
    if count == 2:
        ans = True
        break

print('Yes' if ans else 'No')

