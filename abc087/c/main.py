'''
<方針>
- N=100 なので全探索を行う
- ans の初期値を上全部足して、下移動で (2, N) につくときの合計とする（0 でもよかった）
- 全探索を行い最大値を求めていく
'''

N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

# 答えの初期値
ans = sum(A1) + A2[-1]

# 下に移動する位置を i としたときの、合計値を全探索で求めていく
for i in range(N):
    # 上と下の各範囲の合計値を合計する
    num = sum(A1[:i+1]) + sum(A2[i:])
    ans = max(ans, num)
    
print(ans)

# 計算量 O(N^2)