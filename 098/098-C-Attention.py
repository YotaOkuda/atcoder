N = int(input())
S = input()

# 東西ごとに累積和の配列を用意
west = [0]*(N + 1)
east = [0]*(N + 1)

# 累積和の配列作成
for i in range(N):
    if S[i] == 'W':
        west[i+1] = west[i] + 1
        east[i+1] = east[i]
    else:
        east[i+1] = east[i] + 1
        west[i+1] = west[i]

ans = N

# あるリーダーの時、違う方向を向いている人を計算
# 0から累積和をしているのでS[i]はwest/east[i+1]に対応
for i in range(N):
    if S[i] == 'W':
        no_w = west[i+1] - 1  # 現在のwより左のwの数
    else:
        no_w = west[i+1]      # 現在のeより左のwの数
    
    no_e = east[-1] - east[i+1]  # 現在のeから最後までのeの数
    
    no = no_w + no_e
    ans = min(ans, no)

print(ans)


# 計算量 O(N) < 10^8 
# max.N = 3 * 10^5