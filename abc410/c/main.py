'''
<方針>
- query3 を愚直に行うと計算量は全体で、O(Qk) となりTLE
- どれだけローリングするかをoffset（初期値 = 0）として表す
- ローリング後のAi は A[(p + offset) % N] と表すことができる
- (offset + k) % N でoffset を更新する
'''

N, Q = map(int, input().split())

A = list(range(1, N + 1))

offset = 0
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, x = query[1] - 1, query[2]
        A[(p + offset) % N] = x
    elif query[0] == 2:
        p = query[1] - 1
        print(A[(p + offset) % N])
    elif query[0] == 3:
        k = query[1]
        offset += k
        offset = offset % N

# 計算量 O(N + Q)
