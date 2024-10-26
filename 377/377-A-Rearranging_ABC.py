# 入力文字列をソート（sortedを使用するとリスト形式になる）
S = sorted(input())

S = ''.join(S)

# 文字列が 'ABC' になりえるかを判定
if S == 'ABC':
    print('Yes')
else:
    print('No')
    
# 計算量 O(1)