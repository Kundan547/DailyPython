n = int(input("Enter a number: "))
arr = []
for i in range(1, n + 1):
    if n % i  == 0: arr.append(i)
for j in arr: print(j, end = ' ')