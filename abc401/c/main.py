import sys

N, K = map(int, input().split())

mod = 10 ** 9

if N < K:
    print(1)
    sys.exit()
elif N == K:
    print(K)
    sys.exit()

A = [1] * (N + 1)
A[K] = K
total_value = K * 2
for i in range(K + 1, N + 1):
    left_value = A[i - K - 1]
    A[i] = total_value - left_value
    
    A[i] = A[i] % mod
    
    total_value = A[i] * 2


print(A[N])