from itertools import product

# 数列AのサイズNを仮に3としておく
N = 3
for A in product(range(2), repeat=N):
    print(list(A))