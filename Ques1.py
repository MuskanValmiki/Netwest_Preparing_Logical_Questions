# import requests
# from bs4 import BeautifulSoup
# # import json
# page = requests.get("https://www.w3schools.com/")
# soup = BeautifulSoup(page.text,"html.parser")
# # print(soup,'@@@@@@@@@@@@@@@@@')
# def scrape_top_list():
#     # list = []
#     # div = soup.find("div",class_ = "body_main container")
#     h1=soup.find("h1",class_="learntocodeh1").get_text()
#     # print(h1,'@@@@@@@@@@@@@@@@@@@@@@@@')
#     h3=soup.find("h3",class_="learntocodeh3").get_text()
#     # print(h3,'########################')
#     input_=soup.find("input")
#     # print(input_,'$$$$$$$$$$$$$$$$$$')
#     div=soup.find("div",class_="w3-col l6 w3-center")
#     # print(div,'&&&&&&&&&&&&&&&&&&&&&&&&&&')
#     H1=div.find("h1").get_text()
#     # print(H1,'!!!!!')
#     p=div.find("p").get_text()
#     # print(p,"*******************")
#     a=div.find("a",class_="w3-button tut-button")["href"]
#     # print(a,'^^^^^^^^^/^^^^^^')
#     data=soup.find("div",class_="w3-code cssHigh notranslate green-border")
#     print(data,'%%%%%%%%%%%%%%%%%%%')
    
# scrape_top_list()

from re import A


num=24
num=34
print(num)
# updating

a=12
b=23
c=a=12
a=b=23
b=c=12
print(a)
print(b)
# a=23 b=12 swaping

a=25
b=45
a,b=b,a
print(a,'*')
print(b,'@')
# interchanging 