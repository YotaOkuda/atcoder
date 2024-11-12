N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(max(A) + max(B))

# 合計の最大値を求める(2重for文で)と計算量は O(N^2)となるので
# 数列ごとの最大値を求める

# 計算量 O(N)