N, M, Q = map(int, input().split())

a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    #上から順番に代入していく
    a[i], b[i], c[i], d[i] = map(int, input().split())

result = 0
def rec(A):
    if len(A) == N:
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                break
            else:
                count = calc(A)
                result = (result, count)
        print(result)
        return
    
    for v in range(1, M + 1):
        A.append(v)
        rec(A)
        A.pop()
        

def calc(A):
    sum = 0
    for i in range(Q):
        if A[b[i] - 1] - A[a[i] - 1] == c[i]:
            sum += d[i]
    
    return sum

rec([])