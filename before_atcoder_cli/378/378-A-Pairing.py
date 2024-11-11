'''
<方針>
- ボールの色は 4 種類しかないので、各種類ごとに何個あるかカウントする
- 2 つ選んで捨てるので、2 のペアの数を出力する
'''

A  = list(map(int, input().split()))

# 各種類ごとに何個あるかカウントするリスト
counts = []
# 各種類ごとに何個あるかカウント
for i in range(1, 5):
    counts.append(A.count(i))

ans = 0
# 2 つペアの数を計算
for count in counts:
    ans += count // 2
    
print(ans)

# 計算量 O(1)