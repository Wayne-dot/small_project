from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

PATH = "C:\Development\chromedriver_win32\chromedriver.exe"
link_for_speed_test = "https://www.speedtest.net/result/14407005650"
TWITTER_LOGIN = "https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ" \
                "%3D%3D%22%7D "


class InternetSpeedTwitterBot:
    def __init__(self, driverpath):
        self.driver = webdriver.Chrome(executable_path=driverpath)
        self.down = 0
        self.up = 0

    def get_internet_speed(self, speed_link):
        self.driver.get(speed_link)
        download = self.driver.find_elements(by="css selector", value="div[class='result-data u-align-left']")
        self.down = download[0].text
        self.up = download[1].text

    def tweet_at_provider(self, twit_link):
        self.driver.get(twit_link)


botactivate = InternetSpeedTwitterBot(driverpath=PATH)
botactivate.get_internet_speed(link_for_speed_test)
# use to login to twitter, if need to post anything
botactivate.tweet_at_provider(TWITTER_LOGIN)

# stop the program at the website, to stop the website to quit
input()
