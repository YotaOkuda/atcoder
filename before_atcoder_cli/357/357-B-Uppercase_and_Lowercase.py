S = str(input())

lower = sum(1 for s in S if s.islower())
upper = sum(1 for s in S if s.isupper())

if lower > upper:
    print(S.lower())
elif lower < upper:
    print(S.upper())
else:
    print(S)