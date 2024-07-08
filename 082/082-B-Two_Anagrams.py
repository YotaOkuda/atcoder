s = list(input())
t = list(input())

s.sort()
s = ''.join(s)

t.sort(reverse=True)
t = ''.join(t)

if s < t:
    print('Yes')
else:
    print('No')