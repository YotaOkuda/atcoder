import sys
N = input()
D = list(map(int, input().split()))

pivot, count = 0, 0
D.sort()
if(len(D)%2 != 0):
    print(0)
    sys.exit()
else:
    pivot = len(D)//2 - 1

while(D[pivot] < D[pivot + 1]):
    D[pivot] += 1
    count += 1

print(count)