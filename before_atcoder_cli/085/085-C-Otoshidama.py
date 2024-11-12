import sys

N, Y = map(int, input().split())

yukichi = 10000
higuchi = 5000
noguchi = 1000

for a in range(N+1):
    for b in range(N+1):
        for c in range(N+1):
            if a + b + c <= N:
                if a*yukichi + b*higuchi + c*noguchi == Y:
                    print(a, b, c)
                    sys.exit()

print(-1, -1, -1)