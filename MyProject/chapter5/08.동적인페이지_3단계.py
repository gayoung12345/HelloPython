from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 자동 업데이트 
sv = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=sv, options=chrome_options)
# 페이지가 로딩될 때까지 최대 5초를 기다림
driver.implicitly_wait(5) 

### [selenium 기본 설정 코드 붙여넣기] ###

from selenium.webdriver.common.keys import Keys
import time

# 웹페이지 해당 주소  이동
driver.get("https://startcoding-crawling.herokuapp.com/lv2")
time.sleep(2)

# 스크롤 전 데이터 개수 확인
posts = driver.find_elements(By.CSS_SELECTOR, '.post-preview') 
before_count = len(posts)

while True: # 무한 반복
    # 스크롤 내리기
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.send_keys(Keys.END)

    # 스크롤 사이 로딩 시간
    time.sleep(2)

    # 스크롤 후 로딩된 데이터 개수 확인
    posts = driver.find_elements(By.CSS_SELECTOR, '.post-preview') 
    after_count = len(posts)

    # 스크롤 전, 후 개수 같다면 반복 멈춤
    if before_count == after_count:
        break # 반복문 빠져나감

    # 스크롤 전 개수를 업데이트
    before_count = after_count

import openpyxl

# 새로운 엑셀 파일 생성
wb = openpyxl.Workbook()
ws = wb.active # 활성화 된 시트 선택
ws.append(['제목', '설명', '링크']) # 시트 1행에 작성 (헤더)

# 리스트로 만든 데이터를 시트에 행으로 추가
for post in posts:
    title = post.find_element(By.CSS_SELECTOR, '.post-title')
    subtitle = post.find_element(By.CSS_SELECTOR, '.post-subtitle')
    link = post.find_element(By.CSS_SELECTOR, ".post-meta > a")

    data = [title.text, subtitle.text, link.get_attribute('href')]
    ws.append(data)

# 시트 저장
wb.save('chapter5/data.xlsx')
