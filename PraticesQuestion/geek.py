""" 
    Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.
    """
    
def status_check(a, b, flag):
    if (a >= 0 and b < 0 and not flag) or (a > 0 and b >= 0 and not flag) or (a < 0 and b < 0 and not flag):
        return True
    elif a < 0 and b < 0 and flag:
        return True
    return False


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
flag = bool()

print(status_check(a, b, flag))
    