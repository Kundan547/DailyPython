""" 
You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.
    """
    
def cat_hat(str):
  cat = 0 
  hat = 0 
  for i in range(0,len(str)-2):
      if str[i:i+3]=='cat':
          cat=cat+1
      elif str[i:i+3]=='hat':
          hat=hat+1
  if hat==cat:
      return True
  else:
      return False
  
print(cat_hat('thecatandbat'))