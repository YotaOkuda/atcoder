'''
<方針>
- ピザの買い方は 3 つある
  1. A ピザ X 枚、B ピザ Y 枚だけ買う
  2. X, Y 枚の多い方に合わせて AB ピザだけ買う（余分なピザが出る）
  3. X, Y 枚の少ない方に合わせて AB ピザを買い、足りない分 A or B ピザを買う
- これらを計算して最小の値を出力する
'''

A, B, C, X, Y = map(int, input().split())

# A ピザを X 枚買った時の値段
amount_A = A * X
# B ピザを Y 枚買った時の値段
amount_B = B * Y

# X, Y 枚の多い方に合わせて AB ピザだけを買った時の値段
amount_max_AB = C * max(X, Y) * 2

# X, Y 枚の少ない方に合わせて AB ピザを買った時の値段
amount_min_AB = C * min(X, Y) * 2
# 足りない分 A or B ピザを買った時の値段
if X > Y:
    amount_diff = A * abs(X - Y)
else:
    amount_diff = B * abs(X - Y)
    
print(min(amount_A + amount_B, amount_max_AB, amount_min_AB + amount_diff))

# 計算量 O(1)