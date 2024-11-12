'''
<方針>
- 入力された文字列をソートして 'abc' になるか判定する
'''

# 入力された文字をソートして結合
# sorted を使用した場合リストになるので、結合が必要 
S = ''.join(sorted(input()))

# ソートした文字が 'abc' と一致しているか
if S == 'abc':
    print('Yes')
else:
    print('No')
    
# 計算量 O(1)