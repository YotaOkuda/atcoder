'''
<方針>
- 不可能な場合を考える
  - (1) 文字列長の差が 1 より大きい場合（操作は 1 回のみ、1 回の操作で変更できる文字は 1 文字までのため）
  - (2) 文字列長が同じで、違う文字が 2 つ以上
  - (3) 文字列長の差が 1 で、違う文字が出てきた場合に文字列長の長い方の文字を消す回数が 2 回以上
'''

import sys

K = int(input())
S = list(str(input()))
T = list(str(input()))

# 違う文字の出現回数をカウントする
count_diff = 0
i, j = 0, 0

# (1) の条件
if abs(len(S) - len(T)) > 1:
    print('No')
    sys.exit()
    
# (2) の条件
if len(S) == len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            count_diff += 1
        if count_diff >= 2:
            print('No')
            sys.exit()
    print('Yes')
# (3) の条件
else:
    while i < len(S) and j < len(T):
        if S[i] != T[j]:
            count_diff += 1
            if count_diff >= 2:
                print('No')
                sys.exit()
            
            if len(S) < len(T):
                j += 1
            else:
                i += 1
        else:
            j += 1
            i += 1
    print('Yes')

# 計算量 O(min(len(S), len(T))


'''
# (1) の条件
if abs(len(S) - len(T)) > 1:
    print('No')
# (2) の条件
elif len(S) == len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            count_diff += 1
    print('No' if count_diff >= 2 else 'Yes')
# (3) の条件、T の方が長い場合
elif len(S) < len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            T.pop(i)
            count_diff += 1
        if count_diff >= 2:
            print('No')
            sys.exit()
    print('Yes')
# (3) の条件、S の方が長い場合
else:
    for i in range(len(T)):
        if S[i] != T[i]:
            S.pop(i)
            count_diff += 1
        if count_diff >= 2:
            print('No')
            sys.exit()
    print('Yes')
'''