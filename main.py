from bs4 import BeautifulSoup
import lxml
import requests
import re

URL = "https://news.ycombinator.com/"
# referene https://www.crummy.com/software/BeautifulSoup/bs4/doc/

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

article_tag = soup.select(".titleline a")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")

article_upvote = soup.select("[class~=score]")


maxi = 0
for score in article_upvote:
    upvote = int(re.findall(r"\d+", score.getText())[0])
    if upvote > maxi:
        maxi = upvote
        tag = score

print(tag)


















# with open("website.html", encoding="utf8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# all_anchor_tag = soup.findAll(name="a")
#
# for tag in all_anchor_tag:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)

# heading = soup.select(".heading")
# print(heading)