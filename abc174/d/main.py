N = int(input())
C = str(input())

R_count = C.count('R')

ans = 0
# Rの個数をカウント
# R_count + 1(0インデックス始まりなのでコードはR_count)より右のRの個数と操作の回数が等しい
for i in range(R_count, len(C)):
    if C[i] == 'R':
        ans += 1

print(ans)

# 操作２は不要、操作1だけで完結する
# 計算量 O(N)


'''
# 途中まで考えた事 #
import re

N = int(input())
C = str(input())

count = 0
# 操作1はWRのペアをなくすことに等しい
# WRをペアで文字列から除去（操作1を１回に等しい）
wr_index = [m.span() for m in re.finditer('WR', C)]
for i in range(len(wr_index) // 2):
        C = C.replace('WR', '', 2)
        count += 1

w_count = C.count('W')
r_count = C.count('R')
wrr_count = 0

# WRがひとつ残るのでWR..RのRをカウント
for i in range(len(C)):
    if i + 1 < len(C) and C[i] == 'W' and C[i + 1] == 'R':
        j = i + 1
        while j < len(C) and C[j] == C[i + 1]:
            wrr_count += 1
            j += 1       
        
# 状況に応じて操作回数をカウント
if w_count == 1 or r_count ==1:
    count += 1
elif w_count < wrr_count:
    count += w_count
else:
    count += wrr_count
    
print(count)
'''