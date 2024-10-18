n = int(input())
A = list(map(int, input().split()))

B = []
for a in A:
    B.append(a)
    B.sort(reverse=True)
    print(B)
    
print(B)