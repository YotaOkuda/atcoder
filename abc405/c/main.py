'''
<方針>
- A, B, C, D の正数列があるとする
  このときAB + AC + AD + BC + BD + CD =
  A(B + C + D) + B(C + D) + C(D) と変形することが可能である
- A を逆順にし、D, C + D , B + C + D, ... を求めていく
- 累積和で求める
- 各累積和と対応するAi の積の総和が答えとなる
'''

N = int(input())
A = list(map(int, input().split()))

# 累積和を求める
B = [0]
for a in reversed(A):
    B.append(B[-1] + a)

# B[0],B[-1] は使用しない
B = list(reversed(B))
B.pop()
B.pop(0)

# 対応するAi とBi の積の総和を求める
ans = 0
for i in range(N - 1):
    ans += A[i] * B[i]

print(ans)

# 計算量 O(N)
