# 모듈을 가져오는 방법
# 1) import 모듈명           : 모듈 전체를 가져옴
# 2) from 모듈명 import 이름 : 모듈 내에서 필요한 것만 가져옴

# 방법1 예시
#import tkinter
#tkinter.Widget = tkinter.Label(None, text='I love Python!')
#tkinter.Widget.pack()

# 방법2 예시
#from tkinter import *
#Widget = Label(None, text='I love Python!')
#Widget.pack()

Label = 'This is a Label' 
print(type(Label)) # <class 'str'>
from tkinter import *   
print(Label) # <class 'tkinter.Label'

# del 모듈명 : 모듈 삭제

# 삭제한 모듈을 다시 불러오기 (reload)
# from importlib import reload # reload를 먼저 import
# reload(모듈명)