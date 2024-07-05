N = int(input())
A, B, C = map(int, input().split())

ans = 10000

for countC in range(10000):
    for countB in range(10000):
        if (N - (countC*C + countB*B))%A == 0 and countC*C + countB*B <= N:
            countA = (N - (countC*C + countB*B))//A
            if A*countA + B*countB + C*countC == N:
                if countA +countB + countC < ans:
                    ans = countA + countB + countC

print(ans)


# リファクタリング
N = int(input())
A, B, C = map(int, input().split())

ans = 10000

for countA in range(10000):
    for countB in range(10000):
        tmp = countA*A + countB*B   # tmp = C円以外の合計値
        if (N - tmp)%C == 0 and tmp <= N:   # N-tmpがC円で割り切れる、かつ、tmpがN以下（未満だとAとBだけでNを満たすときを考慮できない）
            countC = (N - tmp)//C
            if countA + countB + countC < ans:  # 最小の枚数を更新
                ans = countA + countB + countC

print(ans)

# 計算量O(N^2) = 10^8