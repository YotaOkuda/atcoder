H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = list(str(input()))

is_passing = []
count = 0
H -= 1
W -= 1

X -= 1
Y -= 1
for t in T:
    if t == 'U' and X - 1 >= 0:
        if S[X - 1][Y] != '#':
            X -= 1
            if S[X][Y] == '@' and [X, Y] not in is_passing:
                is_passing.append([X, Y])
                count += 1
                
    if t == 'D' and  X + 1 <= H:
        if S[X + 1][Y] != '#':
            X += 1
            if S[X][Y] == '@' and [X, Y] not in is_passing:
                is_passing.append([X, Y])
                count += 1
            
    if t == 'L' and Y - 1 >= 0:
        if S[X][Y - 1] != '#':
            Y -= 1
            if S[X][Y] == '@' and [X, Y] not in is_passing:
                is_passing.append([X, Y])
                count += 1
        
    if t == 'R' and Y + 1 <= W:
        if S[X][Y + 1] != '#':
            Y += 1
            if S[X][Y] == '@' and [X, Y] not in is_passing:
                is_passing.append([X, Y])
                count += 1

print(X + 1, Y + 1, count)
