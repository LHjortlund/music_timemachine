import requests
from bs4 import BeautifulSoup

URL="https://www.billboard.com/charts/hot-100/"

selected_date=input("what year you would like to travel to in YYY-MM-DD format: ")

response=requests.get(URL+ selected_date)

soup=BeautifulSoup(response.text,"html.parser")

titles=[title.getText(strip=True) for title in soup.select(selector="li ul li h3")]

print(titles)