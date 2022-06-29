#benzeri sınavda çıkmıştı

#Çıktısı 30 olduğuna göre tek satırlık kodu yazınız?

x=[{"Programlama":43,"veritabanı":12},
   {"Programlama":23,"veritabanı":5},
   {"Programlama":12,"veritabanı":13}
  ]

y=sum(v for i in x for k,v in i.items() if k=="veritabanı")    #cevap satırı
