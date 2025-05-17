'''
<方針>
- 先頭から順に見ていく
- A[i] を正しい場所にスワップする
  A[A[i]-1] = A[i], A[i] = A[A[i]-1]
  （例）i=0, A[0] = 2 の場合、A[1] = A[0], A[0] = A[1]（index は0 始まりのため）
'''
N = int(input())
A = list(map(int, input().split()))

count = 0
ans = []
i = 0
while i < N:
    if A[i] != i + 1:
        j = A[i] - 1
        A[i], A[j] = A[j], A[i]
        ans.append((i + 1, j + 1))
    else:
        i += 1

print(len(ans))
for i, j in ans:
    print(i, j)

# 計算量 O(N)
