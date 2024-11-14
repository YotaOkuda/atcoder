C = [['.', '#', '#'], ['.', '.', '.']]
count = 0
for c in C:
    count += c.count('.')
print(count)