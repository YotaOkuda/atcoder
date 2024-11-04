s = input()
K = int(input())

substring_set = set()

for i in range(1, len(s) + 1):
    start = 0
    end = i
    while end < len(s) + 1:
        substring_set.add(s[start:end])
        start += 1
        end += 1
    
substring_list = sorted(substring_set)

print(substring_list[K - 1])