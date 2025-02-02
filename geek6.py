""" 
    Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).
    
    """
    
def printIncreasingPower(x):
    for i in range(1,x+1):
        if((i*i) <= x ):
            print ( i*i, end = " ")
        elif((i*i)>=x):
            break

print(printIncreasingPower(10))