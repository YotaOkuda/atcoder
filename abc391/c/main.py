

N, Q = map(int, input().split())

bird_list = []
for n in range(N):
    bird_list.append(n)

nest_list = [1] * N
count = 0
s = set()
for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        bird, nest = query[1] - 1, query[2] - 1
        nest_list[bird_list[bird]] -= 1
        if nest_list[bird_list[bird]] == 1 and bird_list[bird] in s:
            s.remove(bird_list[bird])
            
        bird_list[bird] = nest
        nest_list[nest] += 1
        if nest_list[nest] >= 2:
            s.add(nest)
    else:
        print(len(s))