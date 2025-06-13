N = int(input())
T = str(input())

position = [0, 0]
direction = 'East'
for t in T:
    if t == 'S':
        if direction == 'North':
            position[1] += 1
        elif direction == 'South':
            position[1] -= 1
        elif direction == 'East':
            position[0] += 1
        elif direction == 'West':
            position[0] -= 1
    else:
        if direction == 'North':
            direction = 'East'
        elif direction == 'South':
            direction = 'West'
        elif direction == 'East':
            direction = 'South'
        elif direction == 'West':
            direction = 'North'

print(*position)
