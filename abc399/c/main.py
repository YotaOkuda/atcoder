'''
<方針>
- 閉路になってしまうような辺を見つける
- 各頂点が同じグループ（繋がっているか）かを UnionFind木 を用いて判定する
- 重複していれば不要な辺とみなすことができる
'''
'''
N, M = map(int, input().split())
uv = [list(map(int, input().split())) for i in range(M)]

# UnionFind木 を定義
class UnionFind:
    def __init__(self, N):
        self.par = list(range(N))

    # 根を求めるメソッド
    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            # 経路圧縮を行う
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    # 同じグループか判定する
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # 頂点をマージする
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

    # 既に同じグループならば ans をカウント
    if union.same(u, v):
        ans += 1
    # 違うグループならばマージする
    else:
        union.unite(u, v)

print(ans)
'''

from atcoder.dsu import DSU

n, m = map(int, input().split())
uv = [list(map(int, input().split())) for i in range(m)]

ans = 0
union = DSU(n)
for i in range(m):
    u = uv[i][0] - 1
    v = uv[i][1] - 1

    if union.same(u, v):
        ans += 1
    else:
        union.merge(u, v)

print(ans)