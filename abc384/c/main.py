score_list = list(map(int, input().split()))
score_list = list(reversed(score_list))
moji_list = ['E', 'D', 'C', 'B', 'A']

ans = []
for num in range(1<<5):
    score = 0
    moji = ''
    for shift in range(5):
        if 1 & (num>>shift) == 1:
            score += score_list[shift]
            moji = moji_list[shift] + moji
    
    if score > 0:
        ans.append([score, moji])
#print(ans)
ans = sorted(ans, key=lambda x: (-x[0], x[1]))
#print(ans)
for i in range(31):
    print(ans[i][1])
