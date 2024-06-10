# 1) sys
import sys
# sys.ps1 # 현재 사용중인 프롬포트 확인
sys.ps1 = '^^; ' # 프롬포트 변경
print('hello')
print(5 * 3)

print()

# 2) os
import os
print(os.getcwd()) # 현재 작업 디렉토리 출력
print(os.listdir()) # 디렉토리 안 파일과 폴더 리스트 출력
os.chdir('ch01') # ch01디렉토리로 이동
print(os.getcwd()) # 이동확인
print(os.listdir())
os.chdir('..') # 상위 디렉토리로 이동
print(os.getcwd()) # 이동확인

print()

# 3) re
import re, glob
p = re.compile('.*p.*n.*')
for i in glob.glob('*'):
    m = p.match(i)
    if m :
        print(m.group())

print()

# tip) webbrowser
import webbrowser
url = 'http://www.python.org/'
print(webbrowser.open(url)) # 웹브라우저 페이지가 열림

print()

# check) random module
import random
print(random.random()) # 난수(random number) 출력

print(random.randrange(1,7)) # 1~6 난수 출력
print(range(1, 7)) # 1~6 모든 숫자 출력

abc = ['a', 'b', 'c', 'd', 'e']
random.shuffle(abc) # 시퀀스를 랜덤으로 섞음
print(abc) 

menu = '쫄면', '육개장', '비빔밥'
print(random.choice(menu)) # 아무 원소를 하나 뽑아줌

