N, W = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

def rec(n, sw, sv):
    if n == N:
        return sv
    
    result = 0
    
    score = rec(n + 1, sw, sv)
    result = max(result, score)
    
    if sw + w[n] <= W:
        score = rec(n + 1, sw + w[n], sv + v[n])
        result = max(result, score)
    
    return result

print(rec(0, 0, 0))