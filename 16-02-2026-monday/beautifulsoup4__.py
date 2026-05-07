import pandas as pd
import requests
from bs4 import BeautifulSoup

Team_name =[]
Year=[]
Wins=[]
Losses=[]
OTLosses=[]
Win_percentage=[]
Goals_For=[]
Goals_Against=[]


for i in range(2,12):
    url= ('https://www.scrapethissite.com/pages/forms/'+str(i))

    r=requests.get(url)
    # print(r)
    soup = BeautifulSoup(r.text, 'html.parser')

    box = soup.find_all("div",class_="container")

    names = soup.find_all("td",class_="name")

    print(names)

    for i in names:
       name= i.text
       Team_name.append(name)

    print(Team_name)

    year= soup.find_all("td",class_="year")
    for i in year:
        name= i.text
        Year.append(name)
    print(Year)

    wins= soup.find_all("td",class_="wins")
    for i in wins:
      name= i.text
      Wins.append(name)
    print(Wins)

    losses= soup.find_all("td",class_="losses")
    for i in losses:
        name= i.text
        Losses.append(name)
     print(Losses)

    ot_losses= soup.find_all("td",class_="ot_losses")
    for i in ot_losses:
        name= i.text
        OTLosses.append(name)
    print(OTLosses)

    win_percentage= soup.find_all("td",class_="win_percentage")
    for i in win_percentage:
        name= i.text
        Win_percentage.append(name)
    print(Win_percentage)

    Goals_For= soup.find_all("td",class_="goals_for")
    for i in Goals_For:
       name= i.text
       Goals_For.append(name)
    print(Goals_For)

    Goals_Against= soup.find_all("td",class_="goals_against")
    for i in Goals_Against:
        name= i.text
        Goals_Against.append(name)
    print(Goals_Against)


df = pd.DataFrame({"Team_name":Team_name,"Wins":wins,"Losses":losses,"OTLosses":ot_losses,"Win_percentage":win_percentage,"Goals_For":Goals_For,"Goals_Against":Goals_Against})
print(df)

df.to_csv("teams_names.csv")

     # print(soup)
     # while True:
     # np= soup.find("a").get("href")
     # # print(np)
     # cnp = "https://www.scrapethissite.com/pages/forms/" +np
     # print(cnp)

     # url = cnp
     # r= requests.get(url)
     # soup = BeautifulSoup(r.text, 'html.parser')
# rows= soup.find_all('tr',class_='team')
# # print(soup.prettify())
# # teams= soup.find()
#
# teams = soup.find_all('tr', class_='team')
# # Year= soup.find_all('td', class_='teams')
# for teams in teams:
#     print(teams.prettify())


