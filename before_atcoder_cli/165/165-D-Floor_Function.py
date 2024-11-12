A, B, N = map(int, input().split())

# floor(Ax/B) - A * floor(x/B)より、減算部分を最小に抑える
if N < B:
    x = N  # NがBより小さかったらx=N
else:
    x = B - 1  # NがB以上なら、xをBより小さく設定
    
ans = (A*x//B) - A*(x//B)

print(ans)


# 計算量 O(1)