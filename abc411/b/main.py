'''
<方針>
- 各駅を始点としたときの距離をそれぞれリストで保持する（駅1のリスト、駅2のリスト、、、）
- 累積和で距離を計算する
'''

N = int(input())
D = list(map(int, input().split()))

ans = []
for i in range(N - 1):
    dis = 0
    dis_list = []
    for j in range(i, N - 1):
        dis += D[j]
        dis_list.append(dis)
    ans.append(dis_list)

for x in ans:
    print(*x)

# 計算量 O(N^2)
