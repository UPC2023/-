# -*- coding:utf-8 -*-
import requests
import urllib.request
from bs4 import BeautifulSoup
import bs4
import pandas as pd
 
url = 'http://www.gaokao.com/e/20210328/606032dc1b634.shtml'
data=[]
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
 
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip()])
 
 
def printUnivList(ulist, num):
    tplt = "{0:^10}\t.{1:{3}^10}\t.{2:^10}"
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
        data.append([u[0],u[1],u[2]])
       
 
def main():
    uinfo = []
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,140)
 
if __name__ == "__main__":
    main()
    filename = '大学排行榜校友会2021.xlsx'
    df = pd.DataFrame(data[1:], columns=data[0])
    df.to_excel(filename, index=False)


with open('分数线2023.txt', 'r', encoding='utf-8') as file:
    cnt=1
    n=1
    a=[]
    a2=[]
    for line in file:
        if line.strip():
            if cnt==1:
                 a.append(n)
                 a.append(line.strip())
                 cnt+=1
            elif cnt==2:
                a.append(line.strip())
                cnt+=1
            elif cnt==3:
                b=line.split('：')
                #print(b)
                if len(b)==2:
                    a.extend([b[1][0:3]])
                    a2.append(a)
                    a=[]
                    cnt=1
                    n+=1
                
df = pd.DataFrame(a2,columns=['序号', '大学名称', '地区', '分数线'])
df.to_excel('分数线2023.xlsx', index=False)



with open('软科2024.txt', 'r', encoding='utf-8') as file:
    cnt=1
    a=[]
    a2=[]
    for line in file:
        if line.strip():
            if cnt<5:
                if cnt==1:
                    a.append(line.strip())
                elif cnt==2:
                    a.append(line.strip())
                cnt+=1
            elif cnt==5:
                b=line.split()
                if len(b)==4 or len(b)==3:
                    a.extend([b[0],b[2]])
                    a2.append(a)
                    a=[]
                    cnt=1
                else:
                    cnt+=1
            elif cnt==6:
                b=line.split()
                a.extend([b[0],b[2]])
                a2.append(a)
                a=[]
                cnt=1
df = pd.DataFrame(a2,columns=['排名', '大学名称', '省份', '评分'])
df.to_excel('软科2024.xlsx', index=False)
