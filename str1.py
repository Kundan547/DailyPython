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
print(data)#It should be return index 0.
