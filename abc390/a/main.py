import sys

A = list(map(int, input().split()))

ans = [1, 2, 3, 4, 5]


for i in range(4):
    copied_A = A[:]
    copied_A[i], copied_A[i + 1] = copied_A[i + 1], copied_A[i]
    if copied_A == ans:
        print('Yes')
        sys.exit()

print('No')