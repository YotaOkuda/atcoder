a, b = map(int, input().split())

ans = -1
for price in range(10000):
    tax_a = price*8//100
    tax_b = price*10//100

    if tax_a == a and tax_b == b:
        ans = price
        break

print(ans)

#消費税上限は1-100まで➡︎