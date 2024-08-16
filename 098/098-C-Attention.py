N = int(input())
S = input()

west = [0]*(N + 1)
east = [0]*(N + 1)

for i in range(N):
    if S[i] == 'W':
        west[i+1] = west[i] + 1
        east[i+1] = east[i]
    else:
        east[i+1] = east[i] + 1
        west[i+1] = west[i]

print(west)
print(east)

ans = N
for i in range(1, N):
    if S[i] == 'W':
        no_w = west[i] - 1
    else:
        no_w = west[i]
    
    no_e = east[-1] - east[i]
    
    no = no_w + no_e
    ans = min(ans, no)

print(ans)