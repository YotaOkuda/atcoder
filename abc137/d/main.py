N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

sorted_AB = sorted(AB, key=lambda x:(x[1], x[0]), reverse=True)

print(sorted_AB)
