def remove_char(s1, s2):
    dict = {
        ord(s2) : None
    }
    print(s1.translate(dict))
    
    
s1 = input("Please give me String: ")
s2 = input("PLease give a character to remove from given string: ")

remove_char(s1, s2)