from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 브라우저 꺼짐 방지
chrome_options = Options() # options object 생성
chrome_options.add_experimental_option("detach", True) # 꺼짐 방지 설정

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 자동 업데이트 
sv = Service(executable_path=ChromeDriverManager().install()) # 크롬 드라이버를 자동으로 install하고 service object 생성
driver = webdriver.Chrome(service=sv, options=chrome_options) # 크롬 드라이버 객체 생성(크롬 브라우저를 제어할 수 있음), 드라이버 생성 시 옵션 추가

driver.implicitly_wait(15) # 페이지가 로딩될 때까지 최대 15초를 기다림

### 여기까지가 selenium 기본 설정 코드 ###

# 웹페이지 해당 주소 이동
driver.get("https://startcoding-crawling.herokuapp.com/")

title = driver.find_element(By.CSS_SELECTOR, '.site-heading > h1') # 크롬 드라이버로 css 선택자가 '.site-heading > h1'인 태그 찾기
print(title.text) # 찾은 태그의 텍스트만 출력

# 창 꺼짐 방지
input()
