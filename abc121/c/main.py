import sys

N, M = map(int, input().split())
lis = []
for i in range(N):
    a, b = map(int, input().split())
    lis.append([a, b])
lis_sorted = sorted(lis)

sum_price = 0
sum_drink = 0

for x, y in lis_sorted:
    for i in range(1,y+1):
        sum_price += x
        sum_drink += 1
        if(sum_drink == M):
            print(sum_price)
            sys.exit()