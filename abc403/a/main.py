'''
<方針>
- 奇数番目（インデックスでは偶数番目）の要素の合計を計算する
'''

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(0, N):
    if i % 2 == 0:
        ans += A[i]

print(ans)

# 計算量 O(N)
