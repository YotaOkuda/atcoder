'''
<方針>
- いもす法を用いて、N以下の各要素が何回出現しているかを計算する
- 要素の大きさ <= 出現回数 を満たしている中で、一番大きい要素が答え
'''

N = int(input())
A = list(map(int, input().split()))

num = [0] * (N + 1)

for a in A:
    num[0] += 1
    if a + 1 < N + 1:
        num[a + 1] -= 1

count = 0
for i in range(N + 1):
    num[i] = count + num[i]
    count = num[i]

ans = 0
for i in range(N + 1):
    if i <= num[i]:
        ans = max(ans, i)

print(ans)

# 計算量 O(N)
