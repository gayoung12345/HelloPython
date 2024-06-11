import requests
from bs4 import BeautifulSoup

respose = requests.get("https://startcoding-crawling.herokuapp.com/lv1")
html = respose.text
soup = BeautifulSoup(html, 'html.parser') 
#print(soup)
posts = soup.select(".post-preview")

#print(posts)
#print(len(posts))

for post in posts:
    title = post.select_one('.post-title')
    subtitle = post.select_one('.post-subtitle')
    link = post.select_one(".post-meta > a")

    print("=====제목=====")
    print(title.text + "\n")

    print("=====설명=====")
    print(subtitle.text + "\n")
    
    print("=====링크=====")
    print(link.attrs['href'] + "\n")
    