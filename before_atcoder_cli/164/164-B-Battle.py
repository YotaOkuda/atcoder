A, B, C, D = map(int, input().split())

'''count1, count2 = 0, 0
while A > 0 and C > 0:
    C -= B
    count2 += 1
    if C <= 0:
        break
    A -= D
    count1 += 1
    if A <= 0:
        break

if count1 < count2:
    print('Yes')
else:
    print('No')'''

#別解
while A > 0 and C > 0:
    C -= B
    if C <= 0:
        print('Yes')
        break
    A -= D
    if A <= 0:
        print('No')
        break