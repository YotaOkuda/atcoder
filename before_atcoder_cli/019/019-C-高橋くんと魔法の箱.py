N = int(input())
A = list(map(int, input().split()))

appeared = set()
ans = 0

for a in A:
    while a % 2 == 0:
        a = a // 2
        
    if a not in appeared:
        ans += 1
        appeared.add(a)
    
print(ans)


# 計算量 O(N)