N = int(input())
A = sorted(list(map(int, input().split())))

ans = 0
flag = False
count = 0
for i in range(1, N):
    count += A[0] * A[i]

for i in range(1, N):
    if A[i] == A[i - 1]:
        plus = count - A[i] * 2
        ans += plus 
    else:
        if i == 1:
            ans += count
        plus = 0
        for j in range(i + 1, N):
           plus += A[i] * A[j]
        ans += plus

    count = plus

print(ans)
