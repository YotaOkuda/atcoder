M = int(input())

N = 20

# 3^i が何個使うかカウントする箱
ans = [0] * N

for i in range(N):
    ans[i] += M % 3  # Mを3で割った余り
    M = M // 3       # Mを3で割った商をMとする

# 3^iの合計個数を出力
print(sum(ans))

for i in range(N):
    if ans[i] > 0:
        for _ in range(ans[i]):
            print(i, end=' ')
            
# 三進法を適用

# 計算量 O(log M)