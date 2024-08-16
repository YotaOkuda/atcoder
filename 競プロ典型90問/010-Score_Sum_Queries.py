N = int(input())

score1 = [0]*(N + 1)
score2 = [0]*(N + 1)

for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        score1[i+1] = score1[i] + P  # 1組の場合P点を加算する
        score2[i+1] = score2[i]      # 2組は累積和を引き継ぐ
    else:
        score2[i+1] = score2[i] + P  # 2組の場合P点を加算する
        score1[i+1] = score1[i]      # 1組は累積和を引き継ぐ

Q = int(input())

for i in range(Q):
    L, R = map(int, input().split())
    ans1 = score1[R] - score1[L-1]  # L-RまでなのでLも含める。よってL-1
    ans2 = score2[R] - score2[L-1]
    print(ans1, ans2)

print(score1)
print(score2)