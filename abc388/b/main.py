N, D = map(int, input().split())
sneaks = [list(map(int, input().split())) for l in range(N)]

for i in range(1, D + 1):
    maxWeight = 0
    for sneak in sneaks:
        maxWeight = max(maxWeight, sneak[0] * (sneak[1] + i))
        
    print(maxWeight)
    
