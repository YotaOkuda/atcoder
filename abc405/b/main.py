N, M = map(int, input().split())
A = list(map(int, input().split()))

underM = set()
flag = False
ans = 0
for i in range(N):
    a = A[i]
    if a <= M:
        underM.add(a)
    for j in range(1, M + 1):
        if j not in underM:
            break
        elif j == M:
            flag = True
    
    if flag:
        ans = N - i
        break

print(ans)
