'''
<方針>
- A の先頭からM 以下の数値をset に追加していく
- 毎回 set に1 以上 M 以下の整数がすべて含まれているかを判定する
- すべて含まれているならば、そのインデックスまで削除すれば条件が満たされないということなので、N - i となる
'''

N, M = map(int, input().split())
A = list(map(int, input().split()))

underM = set()
flag = False
ans = 0
for i in range(N):
    a = A[i]
    if a <= M:
        underM.add(a)
    for j in range(1, M + 1):
        if j not in underM:
            break
        elif j == M:
            flag = True
    
    if flag:
        ans = N - i
        break

print(ans)

# 計算量 O(N * M)
