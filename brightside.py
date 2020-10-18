import requests
from bs4 import BeautifulSoup
import json


page=requests.get("https://brightside.me/inspiration-psychology/why-we-always-want-to-buy-more-new-things-and-how-to-deal-with-it-798859/")

pageSoup=BeautifulSoup(page.text, "html.parser")



s=pageSoup.find_all("script")[2]
print(len(s))
sText=str(s)[47:]
sText=sText[:-20]

data=sText
with open("bright.txt","w") as f:
    f.write(str(data))
    f.close()
