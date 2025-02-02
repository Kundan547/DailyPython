a=input()
b=input()
def anagram(a,b):
  for i in a:
    if a.count(i)==b.count(i):
      return print(f'{a} and {b} are anagram')
    else:
        return print(f'{a} and {b} are not anagram')
    
anagram(a,b)