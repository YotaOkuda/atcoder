N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    C.append(row[0])
    A.append(row[1:])
    
    
ans = sum(C) + 1

for num in range(1 << N):
    # 各参考書についての理解度
    sum_score = [0] * M
    # 各参考書を購入したときの合計金額
    sum_money = 0
    
    for shift in range(N):
        # その書籍について購入する（=1）ならば
        if 1 & (num >> shift) == 1:
            # その書籍の理解度を足す
            sum_score = [x + y for x, y in zip(sum_score, A[shift])]
            # その書籍の金額を足す
            sum_money += C[shift]
            
    # 参考書の組み合わせに対して、理解度が X 以上であれば
    # 最小の金額を更新する
    if all(score >= X for score in sum_score):
        ans = min(ans, sum_money)

if ans == sum(C) + 1:
    print(-1)
else:
    print(ans)
    

# 計算量 O(2^N * N * M) = 600000 < 10^8