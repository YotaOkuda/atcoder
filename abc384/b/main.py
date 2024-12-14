N, R = map(int, input().split())
list = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    if list[i][0] == 1:
        if 1600 <= R <= 2799:
            R += list[i][1]
    elif list[i][0] == 2:
        if 1200 <= R <= 2399:
            R += list[i][1]

print(R)