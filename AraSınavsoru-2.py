#kodun çıktısı nedir

from functools import reduce
x="abcdefghoprsşyz"
y=reduce(lambda a,b:a.upper()+b.lower(),list(x.strip(" ")))
print(y)
