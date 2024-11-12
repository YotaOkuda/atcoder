# process of solving
N, M = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    
    u -= 1
    v -= 1
    
    G[u].append(v)
    G[v].append(u)
    
            
def serch_load(i, g):
    if :
        return 
    
    for side in g:
        if any(item != i for item in G[side]):
            serch_load(i, G[side])
        else:
            
            
            
for i, g in enumerate(G):
    if serch_load(i, g):
        