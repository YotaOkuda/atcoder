a, b, c = map(int, input().split())

list = [a, b, c]
list = sorted(list)

print(list[1])

# 計算量 O(1)


# ---別解 1---
print(sorted(list(map(int, input().split())))[1])


# ---別解 2---
a, b, c = map(int, input().split())

sorted_numbers = sorted([a, b, c])
print(sorted_numbers[1])