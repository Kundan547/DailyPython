""" 
    Find the First Non-Repeating Character from a Stream of Characters.
    """
    
def first_non_repeating(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in s:
        if count[char] == 1:
            return char
    return None

s = "swiss"
result = first_non_repeating(s)
if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")
