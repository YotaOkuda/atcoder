from collections import deque
import numpy as np
N, Q = map(int, input().split())

# A = deque()

# for a in range(1, N + 1):
#     A.append(a)

A = list(range(1, N + 1))

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A[query[1] - 1] = query[2]
    elif query[0] == 2:
        print(A[query[1] - 1])
    elif query[0] == 3:
        A = np.roll(A, -query[1])
        # A.rotate(-query[1])
        # for j in range(query[1]):
        #     x = A.popleft()
        #     A.append(x)
        # A = A[query[1]:] + A[:query[1]]
