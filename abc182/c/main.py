N = input()
d = len(N)

ans = 100

for num in range(1<<d):
    # 桁を消して作られる数字
    N_tmp = ""
    # 消した個数
    ans_tmp = 0
    
    for shift in range(d):
        # 1 & (numをshift個右シフト)=1ならば
        if 1 & num>>shift == 1:
            # その桁を使う
            N_tmp = N_tmp + N[shift]
        
        # 1 & (numをshift個右シフト)=0ならば
        else:
            # 桁を消した個数をカウント
            ans_tmp += 1
    
    print(f'N_tmp:{N_tmp}')
    
    # N_tmpが空なら
    if N_tmp == "":
        continue
    
    if int(N_tmp) % 3 == 0:
        ans = min(ans, ans_tmp)

if ans == 100:
    print(-1)
else:
    print(ans)
    

# 計算量 O(len(N)^2)