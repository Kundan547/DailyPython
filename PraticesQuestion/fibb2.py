first = 0 
second = 1

n = int(input("Enter a number to generate the fibonachi series: "))
print("Fibonachi series: ")
for i in range(0, n):
    if i <= 1:
        result = i
    else:
        result = first + second
        first = second
        second = result
        print(result)