'''
<方針>
- a, b を順に繋げた数字は最大でも 100100
- '順に繋げた数字/2（平方根をしらべるので 1/2 程度まででよい）' まで整数の平方根があるか確認する
'''

a, b = map(str, input().split())

# 順に繋げた数字
chain_number = int(a + b)
# 整数の平方根があるか判定するフラグ
flag = False

# 平方根を探す
for i in range(1, chain_number // 2):
    if i*i == chain_number:
        flag = True
        break

# 答えを出力
if flag:
    print('Yes')
else:
    print('No')
    
# 計算量 O(5*10^4)