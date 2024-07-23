N, M = map(int, input().split())
H = list(map(int, input().split()))

G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    G[a].append(b)
    G[b].append(a)

ans = 0

for i in range(N):
    flag = True
    for j in G[i]:
        if H[i] <= H[j]:
            flag = False
        
    if flag:
        ans += 1
    
print(ans)

# 計算量 O(N+ M) < 10^8