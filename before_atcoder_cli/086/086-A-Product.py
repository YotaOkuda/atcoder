'''a, b = map(int, input().split())
if a*b%2 == 0:
    print('Even')
else:
    print('Odd')'''

N = input()
A = list(map(int, input().split()))
count = 0
while all(a%2 == 0 for a in A):
    A = [a/2 for a in A]
    count +=1
print(count)