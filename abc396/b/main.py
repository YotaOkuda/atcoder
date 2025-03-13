Q = int(input())

cards = [0] * 100

for q in range(Q):
    query = list(map(int, input().split()))
    # print(query)
    if query[0] == 1:
        cards.append(query[1])
    elif query[0] == 2:
        print(cards[-1])
        cards.pop(-1)