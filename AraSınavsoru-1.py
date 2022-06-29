# kodun çıktısı nedir?

from functools import reduce
x=["Python","Programlama","dili","ile","fonksiyonel","programlama"]
y=len(list(filter(lambda a:len(a)>3, x)))
z=reduce(lambda a,b: a*b,range(1,y+1))
print(z)
     
      
