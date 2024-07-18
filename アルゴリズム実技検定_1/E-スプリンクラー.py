N, M, Q = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

