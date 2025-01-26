sentance = "Python is general purpose, High level, dynamic typed, object priendted programing lanugage."
word = sentance.split()
print(word)

#Other example of it.

Data = "Docker, Kuberenetes, Jenkins, Aws, Grafana, Gitlabs, Git , Github, Python, Java"

#Here we have different types of objects for that.

skils = Data.split(",",2)
print(skils)

#Here the another methods of string lower(), upper(), title(), Find().
word = sentance.lower()
print(word)#it should be return the lower case sentance string.

skils = Data.upper()
print(skils)#It should be return the upper case sentance.

word = sentance.title()
print(word)#It should be return the string in frist word of every single word is capital.


#added both string in single string to perform new methods on it.
skil_set = sentance + Data
print(skil_set)

data = skil_set.find('Python')
#print(data)#It should be return index 0.
data = 'Python'
#INSTEAD OF PRINTING DIRECTLY WE CAN USE CONDITIONS FOR THIS IS THE SUB STRING IS EXIST THEN IT RETURNS TRUE OTHER WISE FLASE.

if skil_set.find(data) != -1:
    print("It exist")
else:
    print("It not exist")

#Lets practise some questions based on these methods for better understanding of python string.

#QUESTION 1 -->
#How find the substring in python?

#Soo question says that find the sub string , we need to usee find() to find the sub string.

test = 'Git is a virsion control system, it manages the history of code , you change while code.'
substring  = test.find('is')
print(substring)

#Soo fix the problem of find() method we can use this.

data = 'Python,Flask,Django,FastAPI'
sub_string = input("Inter the substring to find." )

Index = data.find(sub_string)

if Index != -1:
    extracted_string = data[Index: Index + len(sub_string)]
    print("Extracted string", extracted_string)
else:
    print("Not found")