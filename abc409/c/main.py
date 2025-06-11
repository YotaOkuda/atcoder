'''
<方針>
- 正三角形を作るには、3点が円周上で等間隔に配置されている必要がある。よって、L（円周の長さ）が3の倍数でない場合、正三角形は作れない。
- 点1を位置0に置き、順にD[i]だけ時計回りに進んで他の点の位置を記録する（円周の長さLを超えたら0に戻る = mod L）。
- 各点の位置をL要素の配列で管理し、その位置に点が存在するかをカウントで記録する。
- Lを3で割った間隔 `interval = L // 3` を使い、始点aを [0, interval) の範囲で走査することで、
    - b = a + interval、c = b + interval の3点が円上に正三角形となる可能性がある。
- それぞれの位置に点があるなら、`points[a] * points[b] * points[c]` 通りの正三角形が作れる。
- これをすべてのaについて組み合わせを調べ、加算して答えとする。

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
        
# 計算量 O(N)
