N = int(input())
if N%1000 != 0:
    print((N//1000 + 1)*1000 - N)
else:
    print(N%1000)