def gcp(num1, num2):
    if num2 == 0:
        return num1;
    return gcp(num2, num1 % num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(gcp(num1, num2))