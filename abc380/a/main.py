N = list(input())

count_1 = N.count('1')
count_2 = N.count('2')
count_3 = N.count('3')

if count_1 == 1 and count_2 == 2 and count_3 == 3:
    print('Yes')
else:
    print('No')