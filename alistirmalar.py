from functools import reduce

"""map gezmeyi saglar"""
sayi1 = [1,2,3,4,5]
sayi2 = [6,7,8,9,10,2,4]

veriler = list(map(lambda a,b:a*b,sayi1,sayi2))
print(veriler)

"""zip fermuar gibidir"""
sonuc = list(zip(sayi1,sayi2))
print(sonuc)
""" reduce liste içindeki azaltarak gezer ve karşılaştırma yapar"""
numbers = [10,2,45,4,5,6,210,23,2,99]

def find_max(a,b):
    print(a,b,sep='****')
    if a>b:
        return  a
    return b



sonuc = reduce(lambda a,b:a if a>b else b,numbers)
print(sonuc)

sonuc = filter(lambda a:a>14,numbers)
print(list(sonuc))

#kadir alistirmalar
sifreler = ['ali123.45','veli122','kamilr','gel.123']
print([i if '.' in i else '' for i in sifreler ])

print([i for i in sifreler if '.' in i])

# kesişim
grup1 = ['python','ruby','java','dell','masd']
grup2= ['dart','flutter','python','dell','masd']

kesisim = [i for i in grup1 if ( i in grup2  )]
print( kesisim)
fark12 = [i for i in grup1 if (i not in grup2)]
print(fark12)

#zip ve map
sonuc =dict(zip(sifreler,grup1))
print(sonuc)


print(list(range(-12,34,5)))
newfilter = list(filter(lambda a:len(a)>4, grup1))
print(newfilter)

## cift dongu
newlist = [[i,j]for i in grup1 for j in grup2 if i == j ]
print(newlist,len(newlist))

upper = list(map(lambda a:a.upper(),grup1))
print(upper)
listk = [
    {'programlama':43,'veritabani':12},
    {'programlama': 23, 'veritabani': 5},
    {'programlama': 12, 'veritabani': 13}
]
varlue  = sum(  [c[1] for c in [[v for k,v in i.items() ] for i in listk]])
print(varlue)



sifreler = ['ali123.45','Veli1sdsd22','kamilr','Gel.12sad3']
#içinde . olan ve 6dan fazla karaktei olanı al
news = filter(lambda s:all([any([i.isdigit() for i in s]),any([i.isupper() for i in s]),len(s)>6]),sifreler)
print(list(news))