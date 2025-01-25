import sys

N = int(input())
A = list(map(int, input().split()))

# ans = True

# if len(A) == 2:
#     ans = True
# else:
#     ratio = A[1] / A[0]
#     for i in range(2, N):
#         next_ratio = A[i] / A[i - 1]
#         if ratio != next_ratio:
#             ans = False
#             break

ratio = A[1] / A[0]
make_A = [A[0]]
while len(A) != len(make_A):
    make_A.append(int(make_A[-1] * ratio))

print('Yes' if A == make_A else 'No')

# print('Yes' if ans else 'No')