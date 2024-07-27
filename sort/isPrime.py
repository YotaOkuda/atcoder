import math as m

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    
    sqrtNum = m.floor(m.sqrt(num))
    for i in range(3, sqrtNum + 1, 2):
        if num % i == 0:
            return False
        
    return True

N = int(input())

if is_prime(N):
    print('Prime Number')
else:
    print('Not Prime Number')