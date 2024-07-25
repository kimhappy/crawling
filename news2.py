from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.chosun.com/economy/smb-venture/2024/07/22/SJX5T6NR2FAYJFPSSHJHZCBLAA/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news')
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
text = driver.find_element(By.XPATH, "/html/body").text
lines = text.split('.')
words = []

for i in range(len(lines)):
    line = lines[ i ]
    words = words + line.split(' ')

for i in range(len(words)):
    word = words[ i ]

    if len(word) >= 4:
        print(word)
