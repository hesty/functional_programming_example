from functools import reduce

fibonacci = lambda f: reduce(lambda x , y : x+[x[-1]+x[-2]], range(f-2),[0,1])

print(fibonacci(10000))
