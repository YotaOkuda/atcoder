'''H, A = map(int, input().split())
count = 0

while H > 0:
    if H - A > 0:
        H -= A
        count += 1
    elif H - A == 0:
        H -= A
        count += 1
    else:
        H -= A
        count += 1

print(count)'''

#別解
'''H, A = map(int, input().split())
count = 0
while H > 0:
    H -= A
    count += 1
print(count)'''

#別解
H, A = map(int, input().split())
if H%A == 0:
    print(H//A)
else:
    print(H//A + 1)