import requests
from bs4 import BeautifulSoup

respose = requests.get("https://startcoding-crawling.herokuapp.com/")
html = respose.text
soup = BeautifulSoup(html, 'html.parser') 
#print(soup)
sub_heading = soup.select_one(".subheading") # select_one : 가장 먼저 찾은 태그 객체 하나를 반환
#print(sub_heading)
print(sub_heading.text)