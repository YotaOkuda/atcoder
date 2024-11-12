def fizz_buzz(n):
    if n%15 == 0:
        return 'FizzBuzz'
    elif n%3 == 0:
        return 'Fizz'
    elif n%5 == 0:
        return 'Buzz'
    else:
        return n

N = int(input())
result = 0
for i in range(1, N + 1):
    if fizz_buzz(i) == i:
        result += i

print(result)