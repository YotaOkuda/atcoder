X, K, D = map(int, input().split())

X = abs(X)
q = X // D
r = X % D

if X >= K*D:
    ans = X - K*D
elif (K - q)%2 == 0:
    ans = r
elif (K - q)%2 != 0:
    ans = abs(r - D)

print(ans)


# 計算量 O(1)