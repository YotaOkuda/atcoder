'''N = input()
T, A = map(int, input().split())
H = list(map(int, input().split()))
newT = []

for h in H:
    newT.append(abs((T - h*0.006) - A))

print(newT.index(min(newT)) + 1)'''


#別解
#入力回数分for文で回し，リストのインデックスを対応させる(n回目の時，H[n])
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = 1000
count = 0
for i in range(N):
    if ans > abs(A - (T - H[i]*0.006)):
        ans = abs(A - (T - H[i]*0.006))
        count = i + 1

print(count)