# プログラム1
N = int(input())
t = [0]*(N + 1)
x = [0]*(N + 1)
y = [0]*(N + 1)

# 初期値t=0,(x,y)=(0,0)のため始点は1から
for i in range(1, N+1):
    t[i], x[i], y[i] = map(int, input().split())

flag = True
for i in range(1, N+1):
    T = t[i] - t[i-1]
    X, Y = abs(x[i] - x[i-1]), abs(y[i] - y[i-1])
    if T < X + Y:  # 距離的に不可能
        flag = False
        break

    if T%2 != (X + Y)%2:  # 偶奇が一致しない場合も不可能
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')


# プログラム2
def solve():
    N = int(input())

    # 初期値
    pt, px, py = 0, 0, 0

    for i in range(N):
        t, x, y = map(int, input().split())

        T, X, Y = t - pt, abs(x - px), abs(y - py)

        if T < X + Y:
            return False

        if T%2 != (X + Y)%2:
            return False

        pt, px, py = t, x, y

    return True

print('Yes' if solve() else 'No')

# 計算量 O(N)