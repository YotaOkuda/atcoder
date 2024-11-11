'''A, B, K = map(int, input().split())

for i in range(K):
    if A > B:
        break
    print(A)
    A += 1

b = []
for i in range(K):
    if A > B:
        break
    b.append(B)
    B -= 1

b.sort()
for k in b:
    print(k)'''

#別解
A, B, K = map(int, input().split())
for i in range(A, B + 1):
    if i < A+K or i > B-K:
        print(i)