N, Q = map(int, input().split())

S = input()

n = len(S)
count = [0]*(n + 1)

for i in range(n):
    count[i + 1] = count[i] + S[i-1:i+1].count('AC')

for i in range(Q):
    l, r = map(int, input().split())
    print(count[r] - count[l])