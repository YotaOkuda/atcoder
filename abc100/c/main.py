N = int(input())
A = list(map(int, input().split()))

count = 0
# Aの各要素がそれぞれ2で何回割り切れるかを合計
for a in A:
    while a % 2 == 0:
        a //= 2
        count += 1

print(count)

# 3倍しても2で割り切れる数は変わらない
# 1回だけ2で割って、残りは3倍すればいいので2で割り切れる数を合計する

# 計算量 O(N logAmax)