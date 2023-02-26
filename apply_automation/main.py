from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

email = "wayneting.wc@gmail.com"
word = "chung620"
LOGIN_URL = "https://www.linkedin.com/login"
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3478179310&f_AL=true&geoId=105080838&keywords=python%20developer"
chrome_driver_path = "C:\Development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Login
driver.get(LOGIN_URL)
name = driver.find_element(By.ID, "username")
name.send_keys(email)

password = driver.find_element(By.ID, "password")
password.send_keys(word)

sign_in_buttom = driver.find_element(By.CSS_SELECTOR, "div > button")
sign_in_buttom.click()

time.sleep(5)

# Apply job
driver.get(URL)
time.sleep(5)

list_of_job = driver.find_elements(by="css selector", value="div[class^='job-card-container relative']")

for job in list_of_job:
    link_into = job.find_element(by="css selector", value="a[class^='disabled ember-view']")
    link_into.click()

    time.sleep(2)
    apply_button = driver.find_element(by="css selector", value="button[class^='jobs-apply-button']")
    print(apply_button)
    apply_button.click()

    time.sleep(1000)

    # try, if not, next one

    # next
    # choose
    # review
    # submit
    time.sleep(1)



input(" ")
