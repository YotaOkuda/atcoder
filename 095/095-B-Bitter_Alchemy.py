n, x = map(int, input().split())
'''M = []
n_gram = 0
donut_count = 0
for i in range(n):
    m = int(input())
    M.append(m)
    n_gram += m
    donut_count += 1

rest = x - n_gram
min_gram = min(M)
donut_count += rest//min_gram
print(donut_count)'''

#別解
m = [int(input()) for i in range(n)]
x = x - sum(m)
mini = min(m)
print(n + x//mini)