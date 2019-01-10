from bs4 import BeautifulSoup 
from requests import get

url = "https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc"
response = get(url).content

soup = BeautifulSoup(response, 'html.parser')

#Gets the first page elements only 

total = soup.find_all("div", class_="lister-item mode-advanced")
next_page = soup.find_all("a", class_ = "lister-page-next next-page")
next_page = soup.find("href")

#Pageation 
link = soup.find("a",class_ = "lister-page-next next-page")
link = link.get('href')
response = get("https://www.imdb.com/" + link).content
    