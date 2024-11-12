N = int(input())
A = []
B = []
for n in range(N):
    a = str(input())
    A.append(a)
for n in range(N):
    b = str(input())
    B.append(b)

for i in range(N):
    for j in range(N):
        if(A[i][j] != B[i][j]):
            print(i + 1, j + 1)
            break