n = int(input("Enter a number: "))
temp = 0
reverse = 0

while temp != 0:
    reverse = reverse * 10 + temp % 10
    temp = temp // 10
       
if reverse == n:
    print("Number is palindrom: ")
else:
    print("NUmber is not palindrom: ")