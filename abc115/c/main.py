'''N, K = map(int, input().split())
H = []
for i in range(N):
    H.append(int(input()))

H.sort()
start ,tail= 0, K - 1
min = 10**9
while(tail < len(H)):
    if(H[tail] - H[start] < min):
        min = H[tail] - H[start]
    start += 1
    tail += 1

print(min)'''

#別解
N, K = map(int, input().split())
H = sorted(int(input()) for i in range(N))
ans = 10**100
for i in range(0, N - K + 1, 1):
    ans = min(ans, H[i + K -1] - H[i])
print(ans)