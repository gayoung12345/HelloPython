# 1) pickle : 자료를 파일에 읽고 쓸 수 있는 라이브러리
users = {'kim':'3kid9', 'sum80':'393948', 'lim':'py90390'} # 딕셔너리 생성
f = open('users','wb') # wb: binary모드로 쓰기
import pickle
pickle.dump(users, f) # users를 f에 저장
f.close() # 닫기

# 파이썬이 실행되는 경로에 users파일 생성 확인
import os
print(os.path.exists('users')) # True 

# 생성한 users 파일을 읽어오기
f = open('users', 'rb') # rb: binary모드로 읽기
a = pickle.load(f) # 읽어온 내용을 변수 a에 저장
print(a) # {'kim': '3kid9', 'sum80': '393948', 'lim': 'py90390'}

print()

# 2) glob : 파일의 리스트를 얻는 라이브러리
from glob import glob

# 인자로 받은 패턴과 이름이 일치하는 모든 파일과 디렉토리의 리스트 반환
print(glob('*.exe')) # 현재 디렉토리의 .exe 파일
print(glob('*.txt')) # 현재 디렉토리의 .txt 파일

# 현재 경로가 아닌 다른 경로 조회도 가능
print(glob(r'C:\U*')) # C:\에서 u로 시작하는 디렉토리나 파일 리스트 조회

print()

# 3) os.path : 
from os.path import isdir

for x in glob('*'): # glob()을 이용해 얻은 리스트 조회
    if isdir(x):    # 만약 디렉토리이면
        print(x, '<DIR>')   # 원소 뒤에 문자열'<DIR>'이 같이 출력
    else:
        print(x) # 아니라면 원소만 출력