N = int(input())
A = set(list(map(int, input().split())))

A = list(A)
A.sort()
print(len(A)) 
print(*A)
