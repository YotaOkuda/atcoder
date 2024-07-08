P = int(input())

coin_value = 1
coin_count = 0
coin_mod = 0
i = 1

while P > 0:
    i += 1
    coin_value *= i
    coin_mod = P%coin_value
    coin_count += int(coin_mod/(coin_value/i))
    P -= coin_mod

print(coin_count)