R, G, B = map(int, input().split())
C = str(input())

# 条件以外の色の最小値を表示
if C == "Red":
    print(min(G, B))
elif C == "Green":
    print(min(R, B))
else:
    print(min(R, G))