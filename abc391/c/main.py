'''
<方針>
- 各鳩がどの巣にいるかを管理する bird_list（インデックスが鳩番号を表す）
- 各巣に鳩が何匹いるかを管理する nest_list（インデックスが巣番号を表す）
- set で 2 匹以上いる巣を管理する multiple_nests
- 各クエリを順に処理していく
  クエリ 1 : 移動元の巣を -1 する
            もし 2 匹以上いて、1 匹だけになったらセットから削除
            鳩がどの巣にいるか更新する
            移動先の巣を +1 する
            もし 2 匹以上ならセットに追加する
  クエリ 2 : セットの長さを出力する
'''

N, Q = map(int, input().split())

# 各鳩がどの巣にいるか初期化する
bird_list = []
for n in range(N):
    bird_list.append(n)

# 各巣に何匹鳩がいるかを初期化する
nest_list = [1] * N

# 複数の鳩がいる巣を管理するセット
multiple_nests = set()

# クエリ処理
for q in range(Q):
    query = list(map(int, input().split()))
    
    # クエリが 1 のとき
    if query[0] == 1:
        # インデックスを 0 ベースに揃える（移動する鳩番号、移動先の巣）
        bird, nest = query[1] - 1, query[2] - 1
        
        # 移動元の巣の鳩数を更新
        nest_list[bird_list[bird]] -= 1
        # 複数羽から 1 匹に減った場合、セットから削除
        if nest_list[bird_list[bird]] == 1 and bird_list[bird] in multiple_nests:
            multiple_nests.remove(bird_list[bird])
        
        # 鳩がどの巣に移動したかを記録
        bird_list[bird] = nest
        # 移動先の巣の鳩数を更新
        nest_list[nest] += 1
        # 鳩が複数いるならセットに追加
        if nest_list[nest] >= 2:
            multiple_nests.add(nest)
    # クエリが 2 のとき
    else:
        print(len(multiple_nests))

# 計算量 O(N + Q)