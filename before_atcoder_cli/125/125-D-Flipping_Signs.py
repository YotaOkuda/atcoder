N = int(input())
A = list(map(int, input().split()))

minus_count = 0
min_a = 100000000000
# マイナスの個数と、絶対値の最小値を探索
for a in A:
    if a < 0:
        minus_count += 1
    min_a = min(min_a, abs(a))

ans = 0
# マイナスの個数の偶奇に応じて出力 
if minus_count % 2 == 0:
    for a in A:
        ans += abs(a)
else:
    for a in A:
        ans += abs(a)
    ans -= min_a*2

print(ans)


# 別解
N = int(input())
A = list(map(int, input().split()))

# マイナスの数
num_minus = sum(a < 0 for a in A)

# N個の整数の絶対値の総和、最小値
sum_abs = sum(map(abs, A))
min_abs = min(map(abs, A))

# マイナスの個数の偶奇に応じて出力
print(sum_abs if num_minus % 2 == 0 else sum_abs - min_abs*2)


# 計算量 O(N) < 10^8