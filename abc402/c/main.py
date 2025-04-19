from collections import defaultdict

N, M = map(int, input().split())
food = defaultdict(set)
can_eat = set()
for i in range(M):
    A = list(map(int, input().split()))
    key = A[0]
    food[key].add(set(A[1:]))

B = map(int, input().split())
# for b in range(len(B)):
#     can_eat.add(b)
#     if can_eat in food:

print(food)