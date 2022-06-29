#kodun çıktısı nedir
from functools import reduce

def tester():
   def reducer (b):
      return reduce(lambda i,j: i+j, b)
   return reducer
x=tester()
print (x(range(5)))



