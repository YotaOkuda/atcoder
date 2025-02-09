'''
<方針>
- 見つめている人のゼッケンは Q[P[i] - 1] となる
- ゼッケン順に出力するので同時にゼッケン番号を記録しておく
- ゼッケン番号を key として ans をソートし出力する
'''

'''
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ans = []
index_ans = []
for i in range(N):
  index_ans.append(Q[i])
  ans.append(Q[P[i] - 1])

index_ans, ans = zip(*sorted(zip(index_ans, ans)))

print(*ans)
'''

# 計算量 O(N log N)

'''
<リファクタリング>
- 求める答えを Si とすると、S[Q[i]] = Q[P[i]] が成立する
- ans の各インデックスに見ている人を記録していく
'''

N = int(input())
P = [0] + list(map(int, input().split()))
Q = [0] + list(map(int, input().split()))

ans = [0] * (N + 1)
for i in range(1, N + 1):
  ans[Q[i]] = Q[P[i]]

print(*ans[1:])

# 計算量 O(N)