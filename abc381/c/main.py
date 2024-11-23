'''
<方針>
- 文字列の中に '/' を確認するたびに、その両端が 1, 2 か確認する
  '1/2' のように両端が条件を満たすなら、さらにその両端 '11/22' かどうか確認する
- 条件を満たすたびカウントしていき、最大値を出力
  最終的な文字列の長さは、count * 2 - 1 となる（count の初期値が 1 のため）
'''

N = int(input())
S = str(input())

# '/' は最低 1 つあるので、最小の答え
ans = 1
# 文字列を全部確認する
for i in range(N):
    if S[i] == '/':
        # '/' から探索するインデックスと、条件のカウントを兼ねる
        count = 1
        # 両端が 1, 2 の場合
        while 0 <= i - count and i + count < N and S[i - count] == '1' and S[i + count] == '2':
            # カウントを更新し、さらに両端を探索する
            count += 1
            
        # 最大となる文字列のカウントを更新
        ans = max(ans, count)

# 最大となる文字列の長さを出力
print(ans * 2 - 1)

# 計算量 O(N ^ 2)


# ----- 別解 -----
'''
ans = 1
i = 0
while i < N:
    if S[i] == '/':
        count = 1
        while 0 <= i - count and i + count < N and S[i - count] == '1' and S[i + count] == '2':
            count += 1
        
        i += count
        ans = max(ans, count)
        
    else:
        i += 1
'''