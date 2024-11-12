'''
<方針>
- 条件分岐でレートが小さい方から判断して行く
'''

R = int(input())

# レートごとの条件分岐
if R < 1200:
    print('ABC')
elif R < 2800:
    print('ARC')
else:
    print('AGC')
    
# 計算量 O(1)