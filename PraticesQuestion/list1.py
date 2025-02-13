from collections import Counter

s = "hello world hello everyone"

w_freq = Counter([word for word in s.split()])

print(w_freq)