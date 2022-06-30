# x = ["a1","b1","a1","1a","abc123","1a2b",'b1 ']
# y = list(set(x))
# print(y)

from functools import reduce

x = "Python"

y = [ x[0:i+1] for i in range(0,len(x))]

print(y)