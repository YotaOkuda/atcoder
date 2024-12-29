'''
<方針>
- 1 枚加えて、フルハウスになる 4 枚の状況は以下の 2 通り
  - (1) 2 枚ずつ同じ数字
  - (2) 3 枚同じ数字
- 上記の状況に対応できるように、1 - 14 の数字をカウントする
  - (1) 2 枚同じ数字が 2 回出現するか
  - (2) 3 枚同じ数字が 1 回出現するか
'''
card = list(map(int, input().split()))

# 2 枚同じカードがある場合にカウントする
two_count = 0
# 3 枚同じカードがある場合にカウントする
three_count = 0

# 1 - 14 についてそれぞれカウントしていく
for i in range(1, 14):
    count = card.count(i)
    # 2 つ同じ数字をカウント
    if count == 2:
        two_count += 1
    # 3 つ同じ数字をカウント
    elif count == 3:
        three_count += 1

if two_count == 2 or three_count == 1:
    print('Yes')
else:
    print('No')
    
# 計算量 O(1)