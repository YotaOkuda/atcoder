'''
<方針>
- 素直に全条件を確認する
- 文字列の長さが偶数か
- 'aabbcc' のように同じ文字が 2 連続か
- 'aabbaa' のように同じ文字が 3 回以上出現していないか
'''

S = str(input())

# 文字列の長さ
N = len(S)

# 条件を満たしているかを表すフラグ
flag = True

# 文字列の長さが偶数か
if N % 2 != 0:
    flag = False

# 出現した文字を記録
countString = set()
# i, i + 1 の文字が同じか、文字列を全て確認する
for i in range(1, N // 2 + 1):
    if S[2 * i - 2] != S[2 * i - 1]:
        flag = False
    countString.add(S[2 * i - 2])

# 3 回以上出現していないか
# 条件を満たす文字列の場合、N // 2 種類の文字が出現する
if len(countString) != N // 2:
    flag = False

# 答えを出力
if flag:    
    print('Yes')
else:
    print('No')
    
# 計算量 O(N) = O(1), 1 <= N <= 100