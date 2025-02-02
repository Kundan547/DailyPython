""" Welcome to the part 2 of For Loops in Python. In this question, we'll learn to print characters of a string at even indices.

You are given a string str, you need to print its characters at even indices(index starts at 0).

Note: Please go through the range function to understand how to jump 2 steps.
    """
    
def stringJumper(str):
    for i in range(len(str)):
        if i%2==0:
            print(str[i], end="")
            
str = str(input("Enter a string: "))
print(stringJumper(str))