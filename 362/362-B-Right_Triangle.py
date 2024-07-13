x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

a = (x1 - x2)**2 + (y1 - y2)**2
b = (x3 - x2)**2 + (y3 - y2)**2
c = (x1 - x3)**2 + (y1 - y3)**2

if a == b + c:
    print('Yes')
elif b == a + c:
    print('Yes')
elif c == a + b:
    print('Yes')
else:
    print('No')
