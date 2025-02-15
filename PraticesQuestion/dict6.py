def fun(a):
    a["newkey"] = "new_val" 
d1 = {"key": "old_val"}
d2 = d1.copy() 
fun(d2)
print(d1)       
print(d2)  
