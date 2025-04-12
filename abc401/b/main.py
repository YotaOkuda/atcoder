N = int(input())

ans = 0
is_login = False
for i in range(N):
    S = str(input())
    if S == "login":
        is_login = True
    elif S == "logout":
        is_login = False
        

    if S == "private" and is_login == False:
        ans += 1

print(ans)