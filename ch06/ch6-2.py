import os
os.getcwd() # 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312'
os.listdir() # ['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python312.dll', 'pythonw.exe', 'Scripts', 'tcl', 'vcruntime140.dll', 'vcruntime140_1.dll']
f = open('LICENSE.txt') # 파이썬이 설치된 디렉토리에 있는 LICENSE.txt파일 열기 

# 한 줄씩 읽기 readline()
f.readline() # 'A. HISTORY OF THE SOFTWARE\n'
f.readline() # '==========================\n'

# 반복문을 사용해서 한 줄씩 읽기
for x in range(5): # 5줄
    f.readline()

# 여러줄 읽기 readlines()
f = open('LICENSE.txt')
lines = f.readlines()
lines[:5] # 한 줄이 리스트의 원소로 들어감