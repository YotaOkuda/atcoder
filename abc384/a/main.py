'''
<方針>
- 一文字ずつ見ていき、c1 と一致しなかったら、c2 に置き換える
- S をリスト型で受け取ることで、文字を変更する
'''

N, c1, c2 = map(str, input().split())
S = list(str(input()))

# 文字列を先頭から見ていき、c1 と一致しない場合は、c2 に置き換える
for i in range(int(N)):
    if S[i] != c1:
        S[i] = c2
    
print(''.join(map(str, S)))

# 計算量 O(N)