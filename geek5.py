""" 
    Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
    """
    
def printInDecreasing(x):
    while(x >= 0):
        
        print(x, end=" ")
        
        x -= 1
        
print(printInDecreasing(4))