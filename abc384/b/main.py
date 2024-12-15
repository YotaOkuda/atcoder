'''
<方針>
- Div1 ならレートが、1600 <= R <= 2799 のときに、
- Div2 ならレートが、1200 <= R <= 2399 のときに、レートを更新する
'''

N, R = map(int, input().split())
list = [list(map(int, input().split())) for i in range(N)]

# コンテストを順に処理
for i in range(N):
    # Div1 の場合
    if list[i][0] == 1:
        if 1600 <= R <= 2799:
            R += list[i][1]
    # Div2 の場合
    elif list[i][0] == 2:
        if 1200 <= R <= 2399:
            R += list[i][1]

print(R)

# 計算量 O(N)