X = int(input())

max_result = 1

for x in range(1, X + 1):
    for p in range(2, 100):
        if x**p <= X:
            max_result = max(max_result, x**p)

print(max_result)