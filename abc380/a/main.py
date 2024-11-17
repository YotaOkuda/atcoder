'''
<方針>
- 入力をリストで受け取り、「'1', '2', '3'」それぞれカウントする
- 条件を満たしているならば 'Yes' を出力、満たしていなければ 'No' を出力
'''

N = list(input())

# カウント
count_1 = N.count('1')
count_2 = N.count('2')
count_3 = N.count('3')

# 条件を満たしているか
if count_1 == 1 and count_2 == 2 and count_3 == 3:
    print('Yes')
else:
    print('No')
    
# 計算量 O(1)