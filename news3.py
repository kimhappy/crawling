from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

def get_news_links(keyword, num_results):
    driver = webdriver.Chrome()
    driver.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=' + keyword)
    time.sleep(5)

    def make_selector(nth):
        return '#sp_nws' + str(nth) + ' > div > div > div.news_contents > a.news_tit'

    links = []
    for i in range(1, num_results + 1):
        selector = make_selector(i)
        elems = driver.find_elements(By.CSS_SELECTOR, selector)

        if len(elems) == 0:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            elems = driver.find_elements(By.CSS_SELECTOR, selector)

            if len(elems) == 0:
                continue

        elem = elems[0]
        links.append(elem.get_attribute('href'))

    driver.quit()
    return links

def get_article_words(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # 페이지에서 텍스트 가져오기
    text = driver.find_element(By.XPATH, "/html/body").text

    # 정규 표현식을 사용하여 이상한 문자 제거
    clean_text = re.sub(r'[^\w\s]', '', text)

    # 텍스트를 문장으로 나누기
    lines = clean_text.split('.')
    words = []

    # 문장을 단어로 나누기
    for line in lines:
        words.extend(line.split())

    # 길이가 4 이상인 단어 필터링
    filtered_words = [word for word in words if len(word) >= 4]

    driver.quit()
    return filtered_words

def main():
    keyword = input('무슨 키워드를 검색할까요? ')
    num_results = int(input('몇 개의 검색 결과를 가져올까요? '))

    links = get_news_links(keyword, num_results)
    all_words = []

    for link in links:
        words = get_article_words(link)
        all_words.extend(words)

    for word in all_words:
        print(word)

if __name__ == "__main__":
    main()
