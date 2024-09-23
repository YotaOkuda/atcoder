import math as m

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 最小値に置き換えられる個数
box = K - 1
# 最小値以外の数値を全て最小値にするにはいくつboxが必要か
print(m.ceil((N - 1)/box))


# 計算量 O(1)


# 1つだけWAで通らなかった
import math as m

N, K = map(int, input().split())
A = list(map(int, input().split()))

min_index = A.index(min(A))
left_num = min_index
right_num = len(A) - min_index - 1

ans = 0
if left_num <= box or right_num <= box:
    ans = m.ceil((left_num + right_num)/box)
else:
    ans += m.ceil(left_num/box)
    ans += m.ceil(right_num/box)

print(ans)