def calculate_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

def calculate_lcm(x, y):
    
    hcf = calculate_hcf(x, y)
    return (x * y) // hcf

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    lcm = calculate_lcm(num1, num2)
    print("LCM of", num1, "and", num2, "=", lcm)
    
except ValueError:
    print("Please enter valid integers.")