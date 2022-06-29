#Soru: X dizisindeki kelimeler uzunlugu 3 ten buyukse yazdir degilse a yazdir
a="I lve python language"

print([x[::-1] if len(x)>3 else "a"  for x in a.split(' ') ])
