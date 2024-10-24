N = int(input())
A = list(map(int, input().split()))

# 4 で割り切れる数字をカウント
even_four_count = 0
# 2 で割り切れる数字をカウント
even_two_count = 0
# 奇数の数字をカウント
odd_count = 0

# 各数字がどれにあてはまるかカウントする
for a in A:
    if a % 4 == 0:
        even_four_count += 1
    elif a % 2 == 0:
        even_two_count += 1
    else:
        odd_count += 1


# 2 で割り切れる数字がないとき
if even_two_count == 0:
    if (even_four_count + 1) >= odd_count:  # 「14141」の場合 2 + 1 >= 3
        print('Yes')
    else:
        print('No')
# 2 で割り切れる数字があるとき
else:
    if even_four_count >= odd_count:  # 「14142222」の場合 2 >= 2
        print('Yes')
    else:
        print('No')
        
# 計算量 O(N)