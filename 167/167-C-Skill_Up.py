N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    C.append(row[0])
    A.append(row[1:])
    
print(f'C:{C}')
print(f'A:{A}')