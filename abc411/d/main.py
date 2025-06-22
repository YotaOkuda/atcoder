N, Q = map(int, input().split())

pc = [[] for _ in range(N + 1)] 

for i in range(Q):
    query = list(map(str, input().split()))
    p = int(query[1]) - 1
    if query[0] == '1':
        pc[p] = pc[N]
    elif query[0] == '2':
        pc[p].append(query[2])
    else:
        pc[N] = pc[p]

    print(pc)

print(''.join(pc[N]))
    
