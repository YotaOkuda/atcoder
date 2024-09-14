a, b = map(int, input().split())

ans = 'Positive'

if a <= 0 and 0 <= b:
    ans = 'Zero'
elif a < 0 and b < 0:
    if (a + b)%2 == 0:
        ans = 'Negative'

print(ans)