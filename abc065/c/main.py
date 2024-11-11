import math as m
N, M = map(int, input().split())

# 差が 2 以上の場合は、隣り合うことになる
if abs(N - M) > 1:
    print(0)
# 差が 1 のときは、多い方が外側で固定 → 純粋な組み合わせ
elif N != M:
    print(m.factorial(N) * m.factorial(M) % (10**9 + 7))
# 数が一致する時は、位置の入れ替えが発生 → 組み合わせの 2 倍
else:
    print(m.factorial(N) * m.factorial(M) * 2 % (10**9 + 7))
    

# 計算量 O(N)