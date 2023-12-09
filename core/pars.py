import json
import requests
from bs4 import BeautifulSoup

URL = "https://rezka.ag/page/{0}/"
HEADERS = {"user-agent": 
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36"}

def get_html(url, header):
    responce = requests.get(url, headers=header)
    if responce.status_code == 200:
        return responce.text
    else:
        raise Exception(f"Error in responce code {responce.status_code}")
    
def processing(html):
    soup = BeautifulSoup(html, "lxml").find("div", {"class": "b-content__inline_items"}).find_all("div",
        {"class": "b-content__inline_item"})

    info = []

    for item in soup:
        title = item.find("div", {"class": "b-content__inline_item-link"}).find("a").text
        desc = item.find("div", {"class": "b-content__inline_item-link"}).find("div").text
        years = str(desc).split(",")[0]
        country = str(desc).split(",")[1].strip()
        try:
            janre = str(desc).split(",")[2].strip()
        except Exception:
            janre = "None"
        url = item.find("div", {"class": "b-content__inline_item-link"}).find("a").get("href")
        movie = item.find("div", {"class":"b-content__inline_item-cover"}).find("a").find("span",{"class":
            "cat"}).text
        img = item.find("div", {"class":"b-content__inline_item-cover"}).find("a").find("img").get("src")

        info.append({
            "title": title,
            "years": years,
            "country": country,
            "janre": janre,
            "url": url,
            "movie": movie,
            "img": img
        })
    return info

def PARSRUN(url, header):
    my_list = []
    for page in range(1, 11):
        html = get_html(url.format(page), header)
        source = processing(html)
        my_list.extend(source)
        print(f"Страница {page} спарсилась")

    with open("pars.json", "w") as file:
        json.dump(my_list, file, indent=4, ensure_ascii=False)

    return "Парсинг завершён"

# print(PARSRUN(URL, HEADERS))