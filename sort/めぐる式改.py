N = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]
# N = [1]
def isOK(index, key):
    if N[index] >= key:
        return True
    else:
        return False
    
def binary_search(key):
    left = -1
    right = len(N)

    while abs(right - left) > 1:
        mid = int(left + right/2)
        print(left, mid, right)

        if isOK(mid, key):
            right = mid
        else:
            left = mid
    
    return right

print(binary_search(49))

# self write
'''
def isOK(index, key):
    if N[index] >= key:
        return True
    else:
        return False
        
    
def binary_serch(key):
    left = -1
    right = len(N)
    
    while abs(left - right) > 1:
        mid = int((left + right) / 2)
        
        if isOK(mid, key):
            right = mid
        else:
            left = mid
            
    return right
'''