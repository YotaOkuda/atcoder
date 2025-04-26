N = int(input())

abc = [list(map(int, input().split())) for _ in range(N)]


x = [-1] * N

a, b, c = abc[0][0], abc[0][1], abc[0][2]
dp[0] = max(a, b, c)

def whereMax(a, b, c, x):
    if x == a:
        return a
    elif x == b:
        return b
    else:
        return c

prev_num = whereMax(a, b, c, dp[0])

for i in range(N):
    a, b, c = abc[i][0], abc[i][1], abc[i][2]
    if i - 1 >= 0:
        max_num = max(a, b, c)
        num = whereMax(a, b, c, max_num)
        if prev_num == num:
            if abc[i - 1][prev_num] > max_num:
                max_num =
