X = [10, 12, 45, 3, 22, 84, 60]

# 累積和の配列
num = [0]*(len(X)+1)

# 各累積和を7で割った時のあまりの配列
num_ans = [0]*(len(X)+1)

for i in range(len(X)):
    num[i + 1] = num[i] + X[i]

for i in range(len(num)):
    num_ans[i] = num[i]%7

print(num)
print(num_ans)