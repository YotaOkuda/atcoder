N = int(input())
P = list(map(int, input().split()))

index_list = [x for x in range(N)]

P, index_list = zip(*sorted(zip(P, index_list), reverse=True))

ans = [1]
count = 1
for i in range(1, N):
    if P[i] == P[i - 1]:
        ans.append(ans[-1])
    else:
        ans.append(i + 1)

index_list, ans = zip(*sorted(zip(index_list, ans)))
for i in range(N):
    print(ans[i])