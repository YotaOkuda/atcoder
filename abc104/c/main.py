D, G = map(int, input().split())

problem = []

for i in range(D):
    p, c = map(int, input().split())
    problem.append([i * 100, p, c, i * 100 * p + c])

ans = 0
while ans < G:
    if problem[-1][-1] <= G:
        ans += problem[-1][-1]
        problem.pop(-1)
        continue
    else:
        if G % problem[-1][-1] == 0:
            coin = G // problem[-1][-1]
        else:
            coin = G // problem[-1][-1] + 1
        
        
        