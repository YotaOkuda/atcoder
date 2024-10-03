N, M, Q = map(int, input().split())

a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    #上から順番に代入していく
    a[i], b[i], c[i], d[i] = map(int, input().split())
    

def rec(A):
    if len(A) == N:
        print(A)
        return
    
    for v in range(1, M + 1):
        A.append(v)
        rec(A)
        A.pop()
        
rec([])
'''
N, M, Q = map(int, input().split())

a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    #上から順番に代入していく
    a[i], b[i], c[i], d[i] = map(int, input().split())

def calc(A):
    sum = 0
    for i in range(Q):
        if A[b[i] - 1] - A[a[i] - 1] == c[i]:
            sum += d[i]
    
    return sum

A = [1, 3, 4]
print(calc(A))
'''