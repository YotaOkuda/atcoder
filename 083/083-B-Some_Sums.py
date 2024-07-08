N, A, B = map(int, input().split())

sum = 0
total = 0
for n in range(1, N+1):
    origin_n = n
    while n > 0:
        sum += n%10
        n //= 10

    if A <= sum <= B:
        total += origin_n

    sum = 0

print(total)