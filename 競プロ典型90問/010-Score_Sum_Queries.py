N = int(input())

score1 = [0]*(N + 1)
score2 = [0]*(N + 1)

for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        score1[i+1] = score1[i] + P
        score2[i+1] = score2[i]
    else:
        score2[i+1] = score2[i] + P
        score1[i+1] = score1[i]

Q = int(input())

for i in range(Q):
    L, R = map(int, input().split())
    ans1 = score1[R] - score1[L-1]
    ans2 = score2[R] - score2[L-1]
    print(ans1, ans2)