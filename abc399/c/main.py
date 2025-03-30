'''
<方針>
- Union-Findを使う
'''

N, M = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

print(G)