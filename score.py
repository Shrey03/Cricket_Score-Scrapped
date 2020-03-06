import requests
from bs4 import BeautifulSoup
url = "https://www.cricbuzz.com/cricket-match/live-scores"
response = requests.get(url)

# print(response.text)

soup = BeautifulSoup(response.text , "html.parser")
score = soup.find_all("div" , {"class":"cb-col cb-col-100 cb-lv-main"})
# print(score)


for scores in score:
        try:
            score_title = scores.find("h2" , {"class":"cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr"})
            score_name =  scores.find("a" , {"class":"text-hvr-underline text-bold"})
            score_time = scores.find("div" , {"class":"text-gray"})
            score_news = scores.find("div" , {"class":"cb-lv-scrs-col text-black"})
            print(score_title.get_text())
            print(score_name.get_text())
            print(score_time.get_text())
            print(score_news.get_text())

        except AttributeError :

            pass