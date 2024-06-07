# 1)
import calendar 
c = calendar.TextCalendar()
m = c.formatmonth(2021, 2)  # 2021년 2월 달력을 변수 m에 저장
print(m)

# 2)
import tkinter as tk # tkinker GUI(Graphical User Interface)를 만들기 위한 표준 라이브러리
s = "Life is short\nUse Python"

root = tk.Tk() # 어플리케이션의 루트 창 생성
t = tk.Text(root, height=2, width=13) # 텍스트 위젯 생성하고 루트에 배치, 크기 설정
t.insert(tk.END, s) # 텍스트 위젯에 문자열 s를 삽입 (tk.END:텍스트의 끝)
t.pack() # 화면에 표시
tk.mainloop() # 이벤트 루프(사용자가 종료할 때 까지 꺼지지 않음)

# 3)
c = calendar.TextCalendar()
m = c.formatmonth(2021, 3)

root = tk.Tk()
t = tk.Text(root, height=7, width=20)
t.insert(tk.END, m)
t.pack()
tk.mainloop()