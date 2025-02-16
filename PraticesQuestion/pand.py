def reverse(num):
    if num < 10:
        return num
    else:
        return int(str(num % 10 ) + str(reverse(num // 10)))
    
def is_pand(num):
    if num == reverse(num):
        return True
    else:
        return False
    
    
n = int(input("Enter a number: "))

if is_pand(n):
    print("Number is palindrom: ")
else:
    print("Number is not palindrom: ")