A, B, C = map(int, input().split())

if A == B:
    print(C)
elif A == C:
    print(B)
else:
    print(A)
    
# 計算量 O(1)