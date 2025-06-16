'''
<方針>
- 二重リストで各 Li をまとめる
'''

N, Q = map(int, input().split())
num = []
for n in range(N):
    a = list(map(int, input().split()))
    num.append(a[1:])

ans = []
for i in range(Q):
    s, t = map(int, input().split())
    ans.append(num[s - 1][t - 1])

for x in ans:
    print(x)

# 計算量 O(N + Q)
