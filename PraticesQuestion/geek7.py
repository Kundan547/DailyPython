"""  
    You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.

Note:- You don't have to return anything, you just have to print the array.
    """




def pos(n):
    ## Write the code
    if n>0:
        while(n>0):
            print(n-1,end=" ")
            n-=1
    else:
        print("already zero")
    

    ##Write the code
def neg(n):
    ##Write the code
    if n<=0:
        while(n<=0):
            print(n,end=" ")
            n+=1
    else:
        print("already zero")
        
        
print(pos(4))
print(neg(0))