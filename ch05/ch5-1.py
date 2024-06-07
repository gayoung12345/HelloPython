# 1) math
import math # math 모듈을 가지고 옴

print(math.sqrt(2)) # 2의 제곱근 1.4142135623730951
print(math.sqrt(3)) # 3의 제곱근 1.7320508075688772
print(math.sqrt(4)) # 4의 제곱근 2.0

print(math.pi) # math모듈의 변수 pi의 값 3.141592653589793

print()

# 2) calendar
import calendar # calenddar 모듈을 가지고 옴

calendar.prmonth(2024, 6) # 달력 출력

print()

# 3) tkinter
from tkinter import *
Widget = Label(None, text='I love Python!')
Widget.pack()
