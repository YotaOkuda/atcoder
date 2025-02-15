N, M = map(int, input().split())

G = [[] for _ in range(N)]

count = 0

for i in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1

  if u == v:
    count += 1
  elif (u in G[v]) & (v in G[u]):
    count += 1
  else:
    G[u].append(v)
    G[v].append(u)

print(count)