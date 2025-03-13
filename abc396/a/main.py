N = int(input())
A = list(map(int, input().split()))

ans = 0
prev = A[0]
for i in range(1, N):
    if prev == A[i]:
        ans += 1
        if ans == 2:
            break
    else:
        ans = 0
    prev = A[i]

print('Yes' if ans == 2 else 'No')