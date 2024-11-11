N, M = map(int, input().split())
lis = []
for i in range(M):
    p, y = map(int, input().split())
    lis.append([p, y, i])
lis_sorted = sorted(lis, key=lambda x:(x[0], x[1]))

results = []
y_index, flag = 1, 1
for p, y, i in lis_sorted:
    if(p != flag):
        y_index = 1
        flag = p
    results.append([i, '{:06}'.format(p) + '{:06}'.format(y_index), ])
    y_index += 1

results.sort()
for result in results:
    print(result[1])