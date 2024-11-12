A, B, C = map(int, input().split())

# 解毒剤入りが毒入りより多いか少ないかで条件分け
if A + B + 1 >= C:
    print(B + C)
else:
    print(B + (A + B + 1))
    
# 計算量 O(1)