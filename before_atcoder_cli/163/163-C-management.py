N = int(input())
A = list(map(int, input().split()))

# 社員の部下数をカウントする配列
count = [0] * N
# 誰がどの社員の部下かカウント
for i in A:
    count[i - 1] += 1

for ans in count:
    print(ans)
    

# 社員ごとに毎回カウントして出力すると時間がかかるので
# 最初に一気にカウントしてしまう
# for i in range(N):  # 時間がかかる例
#     print(A.count(i))

# 計算量 O(N)