# selenium 라이브러리의 webdriver 기능을 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 Keys 기능을 import
from selenium.webdriver.common.keys import Keys

# 시간 관련 라이브러리를 import
import time

# 웹 브라우저 (크롬 드라이버) 를 실행한다
driver = webdriver.Chrome()

# 웹 브라우저에 URL 주소를 넣고 이동한다
driver.get('https://www.naver.com/')

# 페이지가 완전히 로딩되도록 3초동안 대기한다
time.sleep(3)

# 검색창의 HTML 요소를 찾는다
search_box = driver.find_element('css selector', '#query')

# 원하는 내용을 검색창에 입력한다
search_box.send_keys('기상청')

# 엔터키를 눌러 검색을 실행한다
search_box.send_keys(Keys.RETURN)

# 페이지가 완전히 로딩되도록 3초동안 대기한다
time.sleep(3)

# 검색 결과 중 첫 번째 요소를 선택한다
first = driver.find_element('css selector', '#main_pack > section.sc_new.sp_nsite._project_channel_site_root._fe_site_collection._prs_vsd_bas > div > div > div.nsite_tit > div > div.nsite_name > a')

# 클릭한다
first.click()

# 기존의 탭을 닫는다
driver.close()

# 새 탭으로 전환한다
driver.switch_to.window(window_name = driver.window_handles[ 0 ])

# 페이지가 완전히 로딩되도록 5초동안 대기한다
time.sleep(3)

# 이건 그냥 스크롤 보여주려고 넣은 예제...
# 100 픽셀 아래로 스크롤
driver.execute_script("window.scrollTo(0, 100);")
time.sleep(1)

# 다시 위로 스크롤
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

# 스크롤을 끝까지 내리려면
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# HTML에서 원하는 정보를 가져온다
# 우리는 최저 기온과 최고 기온을 가져올 것이다
# 각 기온을 가리키는 selector를 분석해보자

# 오늘 최저 기온: #digital-forecast > div.cmp-dfs-slider.hr1-fct.mode-default > div.dfs-daily-slider-body > div > div.dfs-daily-slide-wrap > div:nth-child(1) > div > div > div.daily-minmax > div:nth-child(1) > span
# 오늘 최고 기온: #digital-forecast > div.cmp-dfs-slider.hr1-fct.mode-default > div.dfs-daily-slider-body > div > div.dfs-daily-slide-wrap > div:nth-child(1) > div > div > div.daily-minmax > div:nth-child(2) > span
# 내일 최저 기온: #digital-forecast > div.cmp-dfs-slider.hr1-fct.mode-default > div.dfs-daily-slider-body > div > div.dfs-daily-slide-wrap > div:nth-child(2) > div > div > div.daily-minmax > div:nth-child(1) > span
# 내일 최고 기온: #digital-forecast > div.cmp-dfs-slider.hr1-fct.mode-default > div.dfs-daily-slider-body > div > div.dfs-daily-slide-wrap > div:nth-child(2) > div > div > div.daily-minmax > div:nth-child(2) > span
# ...

# 이를 토대로 n번째 날의 기온을 가져오는 selector를 만드는 함수를 정의한다
def temp_selector(day, temp_type):
    return f'#digital-forecast > div.cmp-dfs-slider.hr1-fct.mode-default > div.dfs-daily-slider-body > div > div.dfs-daily-slide-wrap > div:nth-child({day}) > div > div > div.daily-minmax > div:nth-child({temp_type}) > span'

# 오늘, 내일, 모레의 최저 기온과 최고 기온을 가져온다
for i in range(1, 4):
    # temp_selector 함수를 통해 n번째 날의 최저 기온과 최고 기온을 가리키는 selector를 가져온다
    min_selector = temp_selector(i, 1)
    max_selector = temp_selector(i, 2)

    # 가져온 요소에서 텍스트를 가져온다
    min_temp = driver.find_element('css selector', min_selector).text
    max_temp = driver.find_element('css selector', max_selector).text

    # 출력한다
    print(f'최저 기온: {min_temp}, 최고 기온: {max_temp}')
