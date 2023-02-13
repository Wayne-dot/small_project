import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import ssl

URL = "https://www.amazon.com/ASUS-Display-i7-12650H-Thunderbolt-FX517ZM-AS73/dp/B09RMH9B6F/ref=sr_1_4?crid"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7",
}

sender = "EMAIL_ADRESS"
recieve = sender
password = "PASSWORD"


response = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(response.text, "lxml")

name = soup.find_all("span", id="productTitle")
product_name = name[0].getText().strip()




list = soup.find_all("span", class_="a-price-whole")

com = list[0].getText().split(".")[0].split(",")
string_price = com[0] + com[1]
price = int(string_price)

content = f"{product_name}, price is now $ {price}, here is the link {URL}"

if price > 1000:
    em = EmailMessage()
    em["From"] = sender
    em["To"] = sender
    em["subject"] = "Amazon Price Alert!"
    em.set_content(content)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recieve, em.as_string())
