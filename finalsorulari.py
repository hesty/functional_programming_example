from functools import reduce

structure = [
    {'name': 'a', 'count': 7},
    {'name': 'b', 'count': 12},
    {'name': 'a', 'count': 8},
    {'name': 'a', 'count': 9},
]
val = sum(reduce(lambda a, b: a + b,[ c[1] for c in [[v for k,v in s.items()]for s in structure]]))
print(val)

""""""
a = ['python', 'programlama', 'dili', 'ile', 'fonksiyonel', 'programlama']
b = len(list(filter(lambda a: len(a) > 3,a) ))
c = reduce(lambda a,b: a*b,range(1,b+1))
print(a,b,c)


# create a alphabetical list of the words in the list
a = 'abcdefghijklmnopqrstuvwxyz'
def cal(a,b):
    print(a,b,sep='---')
    return a.upper() + b.lower()
b = reduce(lambda a,b:a.upper()+b.lower(),list(a.strip(' ')))
print(b)
print(list(a.strip('')))


##1) N sayının faktöriyelini alan programı (n sabit olarak düşünülebilir, gerekli kütüphanelerin import edildiğini
#varsayabilirsiniz fonksiyonel programlama araçları ile tek satırda yazınız.
n = 5
a = reduce(lambda a,b:a*b,[i for i in range(1,n+1)])
print(a)
"""
2) x=[“MerhaBA”, “PYTHON”, “pROGRAMLAMA”, “Dili”] gibi bir string dizisini “Merhaba Python Programlama Dili”
şeklinde tek bir stringe dönüştürecek programı en fazla 3 satırda fonksiyonel programlama araçları ile yazınız.
Yardımcı metotlar: title() => stringin baş harfini büyütür, ‘ ’.join(liste) parametre olarak aldığı listedeki stringleri
tek tırnaklar içindeki karakteri kullanarak birleştirir
"""
a = ['pYTHhon', 'ProgramlamA', 'dili', 'ILE', 'fonKsiyonel', 'ProgGramlama']

y = [i.title() for i in a]
strcase = ' '.join(y)
print(strcase)

# terseten tek satır
a = ['pYTHhon', 'ProgramlamA', 'dilid', 'ILE', 'fonKsiyonel', 'kazak','ProgGramlama']
new_a =list(filter(lambda a:a == a[::-1],a))
print(new_a)

## iki listeyi map haline getir
usernames = ['azad','ali','mehmet']
passs = ['1243','4566','57657']
soz = map(lambda a,b:{a:b},usernames,passs)
print(list(soz))

sayi1 = [1,2,3,4,5]
sayi2 = [4,5,6,7,0.5]
z  = list(map(lambda a,b : int(a*b),sayi2,sayi1))
print(z)

"""
, tüm küçük harfleri büyük harflere veya tam tersine dönüştürün.
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
"""
text = "Www.HackerRank.com"
modified = ''.join(list(map(lambda a :a.lower() if a.isupper() else a.upper() ,list(text))))
print(modified)

#Size bir dizi verilir. Dizeyi bir " " (boşluk) sınırlayıcısına ayırın ve - tire kullanarak birleştirin.
a = "this is a string"
a = '-'.join(a.split(' '))
print(a)

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

## karesini al
sayi1 = [1,2,3,4,5]
sayi_square = list(map(lambda b:b**2 ,filter(lambda a: a%2 != 0,sayi1)))
print(sayi_square)

print(''.join([i.__str__() for i in range(1,3)]))


print(''.join([i.__str__() for i in range(1, n + 1)]))