n = int(input())
a = list(map(int, input().split()))
count = 0

'''for n in range(10000):
    if all(i%2 == 0 for i in a):
        count += 1
        a = [j//2 for j in a]
    else:
        break

print(count)'''


#別解1 while
'''while all(i%2 == 0 for i in a):
    a = [j//2 for j in a]
    count += 1

print(count)'''


#別解2 Trueフラグをつける
'''while True:
    flag = True
    for i in range(n):
        if a[i]%2 == 1:
            flag = False

    if not flag:
        break

    a = [j//2 for j in a]
    count += 1

print(count)'''


#別解3 割り切れる数の最小を求める
result = 100

for i in a:
    '''while i > 0:
        if i%2 == 0:
            count += 1
            i //= 2
        else:
            break'''

    while i%2 == 0:
        i //= 2
        count += 1

    result = min(count, result)
    count = 0

print(result)