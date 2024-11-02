'''
<方針>
- クエリごとに日付を qi で割って、あまりが ri と一致するか判定する
- 一致する場合は、そのまま dj を出力
- 一致しない場合は、次に一致する日付を求める
- 次に一致する日付は、増加させて探索（+1）すると TLE になるので、数式で求める
'''

N = int(input())

# ゴミの種類ごとの情報を格納するリスト
gabage = []
# q, r のゴミの情報を取得
for i in range(N):
    q, r = map(int, input().split())
    gabage.append([q, r])


Q = int(input())
# クエリを処理
for i in range(Q):
    t, d = map(int, input().split())
    
    # dj を qi で割った余りを求める
    # [t-1] でゴミの種類を、[0] でゴミの種類の qi を取得できる
    remainder = d % gabage[t-1][0]
    
    # 余りが ri と一致する場合
    if remainder == gabage[t-1][1]:
        print(d)
    # 一致しない場合
    else:
        print(d + (gabage[t-1][1] - remainder) + gabage[t-1][0] * (remainder > gabage[t-1][1]))
        
# 計算量 O(N + Q) = max(O(200))