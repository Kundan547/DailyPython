def Swap_num(a, b):
    if (a == 0 and b == 0) or (a == b or b == a):
        print("Both are same ")
        return -1  
    else:
        a, b = b, a
        
    return a, b 

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

print("Before swap the numbers:", a, b)

swapped_a, swapped_b = Swap_num(a, b)

if swapped_a == -1:
    print("Both numbers are zero; no swap performed.")
else:
    print("After swap the numbers:", swapped_a, swapped_b)
