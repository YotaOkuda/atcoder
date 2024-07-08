import sys
N, M = map(int, input().split())
H = [int(i) for i in input().split()]

count = 0
hands = 0
for h in H:
    hands += h
    count += 1
    if hands > M:
        print(count-1)
        sys.exit()

print(count)