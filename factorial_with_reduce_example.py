from functools import reduce

# factorial with reduce 
n = 5
a = reduce(lambda a,b:a*b,[i for i in range(1,n+1)])

print(a)
