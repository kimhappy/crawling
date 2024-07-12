# 서버에 HTML 파일을 request하는 라이브러리를 import
import requests

# HTML 파일을 파싱하는 라이브러리를 import (bs4라고 줄여서 사용)
from bs4 import BeautifulSoup

# 네이버 증권 서버에 request를 보내고, response를 받는다
# headers는 request를 보낼 때, 추가적으로 보내는 정보를 담고 있다
# User-Agent는 request를 보내는 클라이언트의 정보를 담고 있다
# 어떤 서버는 User-Agent를 통해 request를 보낸 클라이언트가 진짜 브라우저인지 확인하기도 한다
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
resp = requests.get('https://finance.naver.com', headers = headers)

# 받아온 response를 HTML로 파싱한다
soup = BeautifulSoup(resp.text, 'html.parser')

# HTML에서 원하는 정보를 가져온다
# 우리는 '주요 뉴스' 섹션의 제목과 링크들을 가져올 것이다
# selector는 HTML에서 특정 요소를 선택하기 위한 문법이다
# 각 뉴스를 가리키는 selector를 분석해보자

# 첫 번째 뉴스: #content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li:nth-child(1) > span > a
# 두 번째 뉴스: #content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li:nth-child(2) > span > a
# 세 번째 뉴스: #content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li:nth-child(3) > span > a
# ...

# 이를 토대로 n번째 뉴스를 가져오는 selector를 만드는 함수를 정의한다
def news_selector(n):
    return f'#content > div.article > div.section > div.news_area._replaceNewsLink > div > ul > li:nth-child({n}) > span > a'

# 첫 세 개의 뉴스 제목과 링크를 가져온다
for i in range(1, 4):
    # news_selector 함수를 통해 n번째 뉴스를 가리키는 selector를 가져온다
    selector = news_selector(i)

    # select_one 함수는 selector에 해당하는 요소 중 첫 번째 요소를 가져온다
    news = soup.select_one(selector)

    # select 함수는 같은 selector를 가진 요소들을 모두 가져오기 때문에, list로 반환된다
    # news = soup.select(selector)[ 0 ]

    # 가져온 요소에서 텍스트를 가져온다
    print(news.text)

    # 가져온 요소에서 href 속성을 가져온다
    print(news[ 'href' ])

    # 줄바꿈
    print()
