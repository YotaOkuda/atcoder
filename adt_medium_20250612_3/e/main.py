N = int(input())

num = [N]
ans = 0
while num:
    x = num[0]
    ans += x
    if x % 2 == 0 and x // 2 > 1:
        
