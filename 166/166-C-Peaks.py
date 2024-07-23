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

# 各頂点とそれに隣接する頂点の高さを比べる
for i in range(N):
    flag = True
    for j in G[i]:      # 隣接する頂点の探索
        if H[i] <= H[j]:    # 現在の頂点の高さH[i]と隣接する頂点の高さH[j]を比べる
            flag = False    # 隣接する頂点のほうが高ければFalseにする
        
    if flag:        # 現在の頂点が隣接する頂点の中で一番高いとき
        ans += 1
    
print(ans)


# 計算量 O(N+ M) < 10^8