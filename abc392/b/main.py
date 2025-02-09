'''
<方針>
- A をセットで管理することで、存在確認を高速に行う
- 1 ～ N + 1 までの i が A に含まれるかを確認する
'''

N, M = map(int, input().split())
A = set(map(int, input().split()))

# A に含まれない数字を格納するリスト
ans = []
for i in range(1, N + 1):
  if i not in A:
    ans.append(i)

print(len(ans))
print(*ans)

# 計算量 O(N)