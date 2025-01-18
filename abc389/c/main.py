from collections import defaultdict

snake = defaultdict(int)
snake[0] = 0

count = 0
countQ1 = 0

Q = int(input())
for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        countQ1 += 1
        snake[countQ1] = snake[countQ1 - 1] + query[1]
    elif query[0] == 2:
        count += 1
        minus = snake[count]
    else:
        print(snake[query[1] - 1 + count] - snake[count])