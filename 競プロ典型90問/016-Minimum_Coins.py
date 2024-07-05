N = int(input())
A, B, C = map(int, input().split())

rangeA = N//max(A, B, C)
if rangeA > 9999:
    rangeA = 9998

rangeB = N//B
rangeC = N//C
ansA, ansB, ansC = 0, 0, 0
ans = 9999

for countC in range(rangeA + 1, 0, -1):
    for countB in range(0, rangeA - countC):
        for countA in range(0, rangeA - countC - countB):
            if A*countA + B*countB + C*countC == N:
                if countA +countB + countC < ans:
                    ansA, ansB, ansC = countA, countB, countC
                    ans = countA + countB + countC

print(ans)

# rangeCを最初のfor文にしてみる