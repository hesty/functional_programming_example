#Soru: X dizisindeki  kelimelerin tersinin uzunlugu 3 ten buyuk olani yazdir degilse a yazdir
a="I lve python language"

print([x[::-1] if len(x)>3 else "a"  for x in a.split(' ') ])
