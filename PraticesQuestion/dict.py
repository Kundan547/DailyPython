d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

myKeys = list(d.keys())
myKeys.sort()

# Sorted Dictionary
sd = {i: d[i] for i in myKeys}

print(sd)
