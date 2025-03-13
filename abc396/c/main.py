N, M = map(int, input().split())
B = sorted(list(map(int, input().split())), reverse=True)
W = sorted(list(map(int, input().split())), reverse=True)

ans = 0
white_end = 0

for i in range(M):
    white_end = i
    if i >= N:
        break
    if W[i] < 1 or (B[i] + W[i]) < 1:
        break
    # print(B[i], W[i])
    ans += B[i]
    ans += W[i]


for i in range(white_end, N):
    if B[i] < 1:
        break
    ans += B[i]


print(ans)
