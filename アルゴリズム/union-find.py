N, M = map(int, input().split())
uv = [list(map(int, input().split())) for i in range(M)]

class UnionFind:
    def __init__(self, N):
        self.par = list(range(N))
    
    # 根を求める
    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    # 同じ集合に属しているかを判定する
    def sama(self, x, y):
        return self.root(x) == self.root(y)
    
    # 違う集合であれば統合する
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        
        if x == y:
            return
        self.par[x] = y

ans = 0
union = UnionFind(N)
for i in range(M):
    u = uv[i][0] - 1
    v = uv[i][1] - 1
    
    if union.same(u, v):
        ans += 1
    else:
        union.unite(u, v)

print(ans)


# OWN
N, M = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(M)]

class UnionFind:
    def __init__(self, N):
        self.par = list(range(N))
    
    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    def same(self, x, y):
        return self.root(x) == self.root(y)
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        self.par[x] = y

union = UnionFind(N)
ans = 0
for i in range(M):
    u = uv[i][0] - 1
    v = uv[i][1] - 1
    
    if union.same(u, v):
        ans += 1
    else:
        union.unite(u, v)

print(ans)