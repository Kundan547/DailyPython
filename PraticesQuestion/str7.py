def anangram(str1, str2):
    if (sorted(str1) == sorted(str2)):
        return True
    else:
        return False
    
str1 = input("Enter first string: ")

str2 = input("Enter second string: ")

if anangram(str1, str2):
    print("Anangram: ")
else:
    print("Not Anangram")