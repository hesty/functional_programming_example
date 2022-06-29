
urls=["www.firat.edu.tr","www.kartoyunu.com","www.bahissavar.com"]

bans= 'kart bahis aaa'

print([url for url in urls for ban in bans.split() if ban in url])
