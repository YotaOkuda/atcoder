'''
<方針>
- X[i] にあるコマ A[i] で、X[i + 1] までの空きマスを埋める
- 余ったコマは X[i + 1] まで移動させ、A[i + 1] に加算する
- 空きマスを埋められるコマがなければ不可能と判断し、処理を終了
- コマの移動回数は X[i] ごとに求める、O(1) で計算する
  sum(range(1, distance + 1)) だと TLE になる

<参考にした考え方>
- X を基準としてソートする（あらかじめソート済みだと思っていた）
'''

import sys

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

# X を基準としてソートする
sorted_pairs = sorted(zip(X, A))
X, A = map(list, zip(*sorted_pairs))

# 最初のマスにコマがない、マスの数とコマ数が一致しないなど不可能な場合
if 1 not in X or sum(A) != N:
    print(-1)
    sys.exit()

# 操作回数
count = 0
# X[i + 1] の場所に持ち越しのコマ
next_koma = 0
# 可能か不可能か判断するフラグ
flag = True

i = 0
while i < M:
    # コマが置いてある最後尾のマスの場合
    # 残りのマスを埋めるだけ
    if i == M - 1:
        count += (N - X[i] + 1) * (N - X[i]) // 2
        break
    
    # 空きマス
    distance = X[i + 1] - X[i] - 1
    # A[i - 1] から持ち越されたコマを加算
    A[i] += next_koma
    # 手持ちのコマで、空きマスを埋められるか
    if A[i] <= distance:
        flag = False
        break
    
    # 空きマスを埋めるのに必要な操作回数を加算
    count += distance * (distance + 1) // 2
    # count += sum(range(1, distance + 1))
    
    # 余ったコマは、X[i + 1] マスに持ち越し
    next_koma = A[i] - distance - 1
    # 余ったコマをがあれば
    if next_koma > 0:
        # X[i + 1] まで移動させるのに必要な操作回数を加算
        count += (distance + 1) * next_koma
   
    # i を更新
    i += 1
    

# 答えを出力
if flag:
    print(count)
else:
    print(-1)
    
# 計算量 O(M log M), 最初のソートが一番かかる, while の処理は O(M)



# --- 他の人の別解 ---
n, m = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))

if sum(a) != n:
    print(-1)
    exit()

# 1 マス目に全コマがあった場合の操作回数
ans = n*(n+1)//2
num = 0

# x を基準としてソートし、全処理
for idx, cnt in sorted(zip(x, a), key=lambda x: x[0]):
    # コマで埋められるか
    if num < idx-1:
        ans = -1
        break
    # マスを更新
    num += cnt 
    # 既に配置されているコマに対する操作回数を引いていく
    ans -= cnt*idx

print(ans)