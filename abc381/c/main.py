N = int(input())
S = str(input())

ans = 1
for i in range(N):
    if S[i] == '/':
        count = 1
        while 0 <= i - count and i + count < N and S[i - count] == '1' and S[i + count] == '2':
            count += 1
        ans = max(ans, count)

print(ans * 2 - 1)