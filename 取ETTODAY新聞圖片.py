import requests
from bs4 import BeautifulSoup
import json
r = requests.get("https://www.ettoday.net/?from=rf")
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("div.piece img")
n = 0
for i in sel:
    if i["src"][1] == "/" :        
        pic = requests.get('http:'+i["src"])
        img = pic.content
        picsave = open("img/img"+str(n)+".png",'wb')
        picsave.write(img)
        picsave.close()
        n+=1
    else :
        pic = requests.get(i["src"])
        img = pic.content
        picsave = open("img/img"+str(n)+".png",'wb')
        picsave.write(img)
        picsave.close()        
        n+=1
