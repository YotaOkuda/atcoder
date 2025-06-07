'''
<方針>
- 正方形が作れる条件は円周を均等に三分割できる場合
- 0から初めの三分割間隔までを見れば、残りの2点も全て決まる
- TODO：AIに方針を分かりやすく添削してもらう
'''

N, L = map(int, input().split())
D = list(map(int, input().split()))

points = [0] * L

points[0] = 1
dis = 0
for i in range(N - 1):
    dis += D[i]
    if dis >= L:
        dis -= L
    points[dis] += 1

ans = 0
if L % 3 != 0:
    print(0)
else:
    interval = L // 3
    for a in range(interval):
        b = a + interval
        c = b + interval
        if points[a] > 0 and points[b] > 0 and points[c]:
            ans += points[a] * points[b] * points[c]
    print(ans)
        
