n = int(input("Enter a number: "))
def test(n):
    if n == 0:
        return 0
    else:
         return  n % 2 == 0
     
print(test(n))