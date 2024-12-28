#A, B, C, D = map(int, input().split())
card = list(map(int, input().split()))

two_count = 0
three_count = 0
for i in range(1, 14):
    count = card.count(i)
    if count == 2:
        two_count += 1
    elif count == 3:
        three_count += 1

if two_count == 2:
    print('Yes')
elif three_count == 1:
    print('Yes')
else:
    print('No')