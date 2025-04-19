Q = int(input())

menu = []
for i in range(Q):
    query = list(map(int, input().split()))
    # print(query)
    if query[0] == 1:
        menu.append(query[1])
    if query[0] == 2: 
        print(menu[0])
        menu.pop(0)