def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
    
        return fib(num - 1) + fib(num - 2)
    
n = int(input("Enter a number to generate the fibonachi series: "))
print("Fibonachi series is: ")
for i in range(0, n):
    print(fib(i))