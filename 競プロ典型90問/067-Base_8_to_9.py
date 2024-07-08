import sys
n, k = map(int, input().split())

a = ''
if n == 0:
    print(n)
    sys.exit()
n = str(n)
n = int(n, 8)
for i in range(k):
    a = ''
    while n > 0:
        n_mod = n%9
        n = n//9
        a = str(n_mod) + a
    a = a.replace('8', '5')
    n = int(a, 8)
print(a)
