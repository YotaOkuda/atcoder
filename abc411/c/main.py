'''
<方針>
- 裏返す対象が黒から白、白から黒の場合で分けられる
- 黒から白
    - 1 マスなら、-1
    - 対象が左端かつ、その右マスが白なら、-1
    - 対象が右端かつ、その左マスが白なら、-1
    - 対象の両端が黒なら、+1
    - 対象の両端が白なら、-1
- 白から黒（省略）
'''

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# マスが黒かを保持するリスト
is_black = [False] * N
# 連続した黒マスの個数を数える
count = 0

for i in range(Q):
    a = A[i] - 1
    # 黒から白
    if is_black[a]:
        if a == 0:
            if N == 1:
                count -= 1
            elif  not is_black[a + 1]:
                count -= 1
        elif a == N - 1:
            if not is_black[a - 1]:
                count -= 1
        else:
            if is_black[a - 1] and is_black[a + 1]:
                count += 1
            elif not is_black[a - 1] and not is_black[a + 1]:
                count -= 1
    # 白から黒
    else:
        if a == 0:
            if  N == 1:
                count += 1
            elif not is_black[a + 1]:
                count += 1
        elif a == N - 1: 
            if not is_black[a - 1]:
                count += 1
        else:
            if is_black[a - 1] and is_black[a + 1]:
                count -= 1
            elif not is_black[a - 1] and not is_black[a + 1]:
                count += 1

    print(count)
    is_black[a] = not is_black[a]

# 計算量 O(N + Q)


'''
- 境界で管理する方法
'''
N, Q = map(int, input().split())
A = list(map(int, input().split()))

a = [0] * (N + 1)
s = 0

for i in A:
    for j in (i - 1, i):
        old = a[j]
        s += (1 - old) - old
        a[j] = 1 - old
    print(s // 2)

# 計算量 O(N + Q)
