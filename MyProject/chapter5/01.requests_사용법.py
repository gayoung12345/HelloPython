import requests

response = requests.get("http://www.naver.com")

print(response) # http 응답코드
print(response.url) # 요청한 url 주소
print(response.status_code) # 응답코드
print(response.text) # html(문자열)