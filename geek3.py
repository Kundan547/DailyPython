""" Writing for loop in Python is a tad different from C++ and Java counterparts. In this question, we'll learn to print table by using the for loop.

You are given a number N, you need to print its multiplication table.

Note: Please go through the range function to understand why it's useful in for loops.
    """
    
def multiple(N):
    for i in range(1, 10 +1):
        print(i * N)
N = int(input("Enter a number: "))
print(multiple(N))