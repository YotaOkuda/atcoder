'''
<方針>
- '/' を見つけたらその両端が '1', '2' か判定する
- (i:'/'のインデックス, count:'/'からの距離)として
  両端のインデックスを(i - count)と(i + count)で表す
- count は 1 始まりなので、count - 1 が '/' から片側への距離となる
'''

N = int(input())
S = str(input())

ans = 0
for i in range(N):
    if S[i] == '/':
        count = 1
        while 0 <= i - count and N > i + count and S[i - count] == '1' and S[i + count] == '2':
            count += 1

        ans = max(ans, count - 1)

print(ans * 2 + 1)

# 計算量 O(N)
