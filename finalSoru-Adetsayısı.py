a=[{"tür":"su" , "adet":2},{"tür":"kebap" , "adet":2},{"tür":"su" , "adet":5}]
#türü su olanların adet sayısını tek satırda toplamını yazınız
print(sum([item["adet"] for item in a if item["tür"] in "su"]))
