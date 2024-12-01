'''
<方針>
- 文字列 S を後ろから見ていき、'@' なら '.' に変える
- D 日間経過したら終了
'''

N, D = map(int, input().split())
S = list(input())

count = 0
for i in range(N - 1, -1, -1):
    if S[i] == '@':
        S[i] = '.'
        count += 1
        
    if count == D:
        break

print("".join(map(str, S)))

# 計算量 O(N)