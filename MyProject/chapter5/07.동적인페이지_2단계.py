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

# import 구문은 중간에 삽입되어도 동작 가능
from selenium.webdriver.common.keys import Keys
import time

# 웹페이지 해당 주소 이동
driver.get("https://startcoding-crawling.herokuapp.com/lv2")
time.sleep(2) # 2초동안 프로그램 실행 정지

# 스크롤 전 데이터 개수 확인
posts = driver.find_elements(By.CSS_SELECTOR, '.post-preview') # css 선택자가 '.post-preview'인 태그 찾기
before_count = len(posts) # 스크롤 전 데이터 개수 저장

while True: # 무한 반복
    # 스크롤 내리기
    body = driver.find_element(By.CSS_SELECTOR, 'body') # body 태그 선택
    body.send_keys(Keys.END) # END키 한번 누르기(스크롤 내려감)

    # 스크롤 사이 로딩 시간(데이터가 충분히 로딩 될 시간이 필요함)
    time.sleep(2) # 2초동안 프로그램 실행 정지

    # 스크롤 후 로딩된 데이터 개수 확인
    posts = driver.find_elements(By.CSS_SELECTOR, '.post-preview') 
    after_count = len(posts) # 스크롤 후 데이터 개수 저장

    # 스크롤 전, 후 개수 같다면 반복 멈춤
    if before_count == after_count: # 스크롤 전, 후 데이터 개수 비교
        break # 무한 반복문 빠져나감

    # 스크롤 전 개수를 업데이트
    before_count = after_count # 스크롤 전 후 개수가 다르다면 다시 반복을 위해 스크롤 전 개수 변경

for post in posts: # posts: 게시물 태그 리스트
    title = post.find_element(By.CSS_SELECTOR, '.post-title') # 제목
    subtitle = post.find_element(By.CSS_SELECTOR, '.post-subtitle') # 설명
    link = post.find_element(By.CSS_SELECTOR, ".post-meta > a") # 링크

    print("=====제목=====")
    print(title.text + "\n")
    
    print("=====설명=====")
    print(subtitle.text + "\n")
    
    print("=====링크=====")
    print(link.get_attribute('href') + "\n")


    