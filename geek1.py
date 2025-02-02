""" 
    You are familiar with basics of input/output and many other useful things in Python. This module is all about conditional statements like if, elif, else; for, while, etc.

In Python, any conditional statement ends with ':' (proper indentation must be followed while working through loops).

There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false
    """
    
def friends(j_angry, s_angry):
    if(j_angry == s_angry):
        return True
    else:
        return False

j_angry = str(input("Enter first string: "))
s_angry = str(input("Enter second string: "))

print(friends(j_angry, s_angry))