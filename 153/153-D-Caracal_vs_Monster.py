def rec(H):
    if H == 1:
        ans += 1
        
    ans = 0
    rec(H//2)
    ans += 2
    