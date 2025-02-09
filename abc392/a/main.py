'''
<方針>
- 全ての組み合わせを確かめる
'''

A1, A2, A3 = map(int, input().split())

flag = False
if A1 * A2 == A3:
  flag = True
elif A1 * A3 == A2:
  flag = True
elif A2 * A3 == A1:
  flag = True

print('Yes' if flag else 'No')

# 計算量 O(1)