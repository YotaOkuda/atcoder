s = str(input())
s_length = len(s)
while s_length > 0:
    s = s[:-2]
    middle = int(len(s)/2)
    if s[:middle] == s[middle:]:
        print(len(s))
        break