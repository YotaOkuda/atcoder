import re

N = int(input())
C = str(input())

wr_index = [m.span() for m in re.finditer('WR', C)]
#print(wr_index)


count = 0
for i in range(len(wr_index) // 2):
        C = C.replace('WR', '', 2)
        count += 1

print(C)
print(count)

w_count = C.count('W')
r_count = C.count('R')
wrr_count = 0

for i in range(len(C)):
    if i + 1 < len(C) and C[i] == 'W' and C[i + 1] == 'R':
        j = i + 1
        while j < len(C) and C[j] == C[i]:
            wrr_count += 1
            
        
if w_count == 1 or r_count ==1:
    count += 1
else:
    count += wrr_count
    
print(count)