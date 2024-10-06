H = int(input())

def rec(H, N):
    if H == 0:
        return N - 1
        
    return rec(H // 2, N * 2)
    
print(rec(H, 1))


# 計算量 O(logH)



# 別解１
H = int(input())
def rec(H):
    if H == 1:
        return 1
    
    # 2 体に分裂するのに「+1」、N//2 を 2体倒すのに rec(N//2)*2
    return rec(H // 2)*2 + 1
print(rec(H))



# 別解２
H = int(input())

ans = 0
while H > 0:
    ans = ans + (ans + 1)
    H = H // 2
    
print(ans)