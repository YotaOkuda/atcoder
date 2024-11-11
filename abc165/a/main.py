K = int(input())
A, B = map(int, input().split())

exist = False
for i in range(A, B+1):
    if i%K == 0:
        exist = True

print('OK' if exist else 'NG')

#rangeは指定したい数字+1の値にする，range(index-1)になることに注意

'''
#別解
K = int(input())
A, B = map(int, input().split())

x = B//K
n = (A-1)//K
if x-n > 0:
    print('OK')
else:
    print('NG')
'''