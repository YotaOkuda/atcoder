N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    plus = A[i]
    for j in range(i + 1, i + plus + 1):
        if j < N:
            A[j] += 1
            A[i] -= 1

print(*A)