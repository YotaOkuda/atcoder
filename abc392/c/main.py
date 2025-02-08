N = int(input())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Q, P = zip(*sorted(zip(Q, P)))

ans = []
index_ans = []
for i in range(N):
  index_ans.append(Q[i])
  ans.append(Q[P[i] - 1])

index_ans, ans = zip(*sorted(zip(index_ans, ans)))

print(*ans)