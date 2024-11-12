N, M, Q = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
    
    a[i] -= 1
    b[i] -= 1

    
def calc(A):
    sum = 0
    for ai, bi, ci, di in zip(a, b, c, d):
        if A[bi] - A[ai] == ci:
            sum += di
        
    return sum


def rec(A):
    if len(A) == N:
        result = calc(A)
    
        return result
    
    result = 0
    
    prev_number = A[-1] if A else 1
    
    for add in range(prev_number, M + 1):
        A.append(add)
        result = max(result, rec(A))
        A.pop()
        
    return result

A = []
print(rec(A))