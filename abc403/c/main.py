'''
<方針>
- 各ユーザーが保持している閲覧権限をリストの中のセットで管理する
- インデックスで各ユーザにアクセス
- 閲覧権限を保持しているかの確認はセットの 'in' を用いる
- 全ての閲覧権限は文字列 'all' を追加する
'''
N, M, Q = map(int, input().split())

# 各ユーザーの閲覧権限を管るするリスト
auth = [set() for i in range(N)]

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        X = query[1]
        Y = query[2]
        auth[X - 1].add(Y)
    elif query[0] == 2:
        X = query[1]
        auth[X - 1].add('all')
    else:
        X = query[1]
        Y = query[2]
        if Y in auth[X - 1]:
            print('Yes')
        elif 'all' in auth[X - 1]:
            print('Yes')
        else:
            print('No')

# 計算量 O(N + Q)
