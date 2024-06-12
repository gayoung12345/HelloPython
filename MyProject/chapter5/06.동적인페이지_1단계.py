import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding-crawling.herokuapp.com/lv2") # 요청 보내기
html = response.text # 요청한 페이지의 text를 저장
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('.post-preview') # css선택자가 '.post-preview'
print(posts) # 데이터를 가지고 오지 못함