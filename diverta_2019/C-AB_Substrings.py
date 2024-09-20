N = int(input())

count = 0
count_A, count_B = 0, 0
for _ in range(N):
    s = str(input())
    count += s.count('AB')
    if s[-1] == 'A':
        count_A += 1
    if s[0] == 'B':
        count_B += 1

if count_A <= 0 or count_B <= 0:
    ans = count
elif count_A == count_B:
    ans = count + count_A - 1
else:
    ans = count + min(count_A, count_B)
    
print(ans)
# print(f'count:{count}, count_A:{count_A}, count_B:{count_B}')