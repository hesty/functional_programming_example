
from functools import reduce
# Soru 1 == Kodun çıktısı nedir?
print(''.join(map(lambda a:a[::-1] if len(a)>3 else a, "Why do I love python?".split(" "))))
#%%
# Soru 2 == Kodun çıktısı nedir?
print(reduce(lambda a,b:a**b,range(-1,6,2)))

#%%
# Soru 3 == Türü su olan satışların adet sayılarının toplamlarını çıktı olarak veren tek satırlık kodu yazınız.
a = [
     {"tür" : "su", "adet":3},
     {"tür" : "kebap", "adet":4},
     {"tür" : "su", "adet":7}
     ]
print(sum(i["adet"] for i in a if i["tür"]=="su"))
#%%
# Soru 4 == Yasaklı kelimeleri içeren internet sitelerini bir liste halinde çıktı veren kodu yazınız.
urls = ["firat.edu.tr","bahis.com", "kumar.com","kartouyun.com"]
bans = "kart bahis kumar"
yasaklılar = list(filter(lambda a: any([1 if i in a else 0 for i in bans.split(' ')]), urls))
print(yasaklılar)
