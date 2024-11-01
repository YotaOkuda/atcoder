'''
<方針>
- 最大値に合わせる方針
- 最大値との差(diff1, diff2)の差(diff1 - diff2)が
    - 1. 偶数ならば、最大値に変化はない
         差の合計/2 回分操作が必要（真ん中の値を最大値に合わせた後、最小値を操作）
    - 2. 奇数ならば、最大値も更新しなくてはならない
         操作 2 のみで最大値までそろえてから、操作 1 → 操作 2 の 2 回の操作が加わる
'''

A, B, C = map(int, input().split())

max_value = max(A, B, C)

# 最大値との差を計算
if max_value == A:
    diff1 = max_value - B
    diff2 = max_value - C
elif max_value == B:
    diff1 = max_value - A
    diff2 = max_value - C
else:
    diff1 = max_value - A
    diff2 = max_value - B
    
# 最大値との差の差が偶数の場合
if abs(diff1 - diff2) % 2 == 0:
    print((diff1 + diff2) // 2)
# 差が奇数の場合
else:
    # 操作 2 の回数
    plus2_diff1 = diff1 // 2
    plus2_diff2 = diff2 // 2
    
    print(plus2_diff1 + plus2_diff2 + 2)
    
# 計算量 O(1)

# リスト形式で受け取りソートした方が、最大値との差の計算が楽になる