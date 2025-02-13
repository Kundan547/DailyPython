def multi(items):
    total = 1
    
    
    for x in items:
        total *= x
        
    return total

print(multi([1,2,-7,9,-1]))