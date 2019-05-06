import requests
from bs4 import BeautifulSoup
import json
r = requests.get("https://www.ettoday.net/?from=rf")
f = open('test.txt','w',encoding = 'utf8')
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("div.box_2 a")
for i in sel:
    print(i["href"],i.text)
    f.write(i.text+"\n")
f.close()
img = soup.select("div.piece icon_type_video a")
for x in img:
    print(x["src"],x.text)
    