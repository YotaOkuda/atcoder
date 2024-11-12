N, Q = map(int, input().split())

S = input()

# 'AC'をカウントする累積配列を作成
count = [0]*(N + 1)

# ある位置を含めた2文字前に'AC'が含まれているか
for i in range(N):
    count[i + 1] = count[i] + S[i-1:i+1].count('AC')  # S[i:i+2]にするとcount[i+1]とずれてしまう

for i in range(Q):
    l, r = map(int, input().split())
    print(count[r] - count[l])

# 別解
# for i in range(1, N):
#     count[i + 1] = count[i] + (S[i-1:i+1] == "AC")

# 計算量 O(N + Q) < 10^8
# N(max)=10^5, Q(max)=10^5