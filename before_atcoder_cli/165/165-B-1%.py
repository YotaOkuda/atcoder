X = int(input())

a, count = 100, 0
while a < X:
    a += a//100 #int型の切り捨てだとエラー
    count += 1

print(count)