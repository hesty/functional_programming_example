'''
Yazacaginiz bir metot ile metota parametre olarak gelen iki tam sayi arasinda rastgele bir 
sayi donduren metotu random kutuphanesi kullanarak yaziniz. metot parametresiz calistiginda 
ise 0-1 arasi float sayi dondurmeli
'''

import random


def randomNumber(a=None,b=None):
    if a is None or b is None:
        return random.random()
    return random.randint(a,b)

print(randomNumber())
print(randomNumber(1,5))



