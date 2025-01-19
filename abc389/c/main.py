'''
<方針>
- 連想配列にヘビのつなぎ目を記録していく
  （例）0:0, 1:一番目の最後尾, 2:二番目の最後尾
- 毎回クエリ 2 のたびに、配列全体に処理をすると TLE となる
- count = クエリ 2 の回数（ヘビを除く回数が分かっていればクエリ 3 で出力するヘビの場所も分かる）
  snake[クエリ 3 の値 - 1 + count] = 出力対象のヘビ
  （例）count = 2, クエリ 3 = 4, snake[4 - 1 + 2] = snake[5]
- snake[count] = その時点でのこれまでヘビが抜けた長さ
- snake[query[1] - 1 + count] - snake[count] がクエリ 3 の時の対象のヘビの長さを表す
'''

from collections import defaultdict

# 連想配列を定義
snake = defaultdict(int)
snake[0] = 0

# クエリ 2 の回数表す
count = 0
# 連想配列のインデックスを表す
countQ1 = 0

Q = int(input())

# クエリを一つずつ処理
for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        countQ1 += 1
        snake[countQ1] = snake[countQ1 - 1] + query[1]
    elif query[0] == 2:
        count += 1
        # minus = snake[count]
    else:
        print(snake[query[1] - 1 + count] - snake[count])

# 計算量 O(Q)