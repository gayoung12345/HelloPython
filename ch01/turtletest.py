import turtle # 거북이그림 라이브러리
import random # 랜덤 숫자 라이브러리

## 함수 선언 부분 ## 
# 왼쪽 클릭
def screenLeftClick(x, y):	
	global r, g, b	# 거북이펜 색상 변수 선언
	turtle.pencolor((r, g, b)) # 거북이펜 색상 
	turtle.pendown() # 펜이 내려감(그려짐)
	turtle.goto(x, y) # 클릭한 좌표로 거북이가 이동

# 오른쪽 클릭
def screenRightClick(x, y): 
	turtle.penup() # 거북이펜 올라감(안 그려짐)
	turtle.goto(x, y) # 클릭한 좌표로 거북이가 이동

# 휠 클릭
def screenMidClick(x, y):
	global r, g ,b	#거북이펜 색상 변수 선언
	tSize = random.randrange(1, 10) # 거북이 크기 랜덤 (1~10)
	turtle.shapesize(tSize) # 거북이의 크기 설정
	r = random.random() # 색상 랜덤 설정 r
	g = random.random() # 색상 랜덤 설정 g
	b = random.random() # 색상 랜덤 설정 b

## 변수 선언 부분 ##
pSize = 10	# 펜 사이즈 설정 
r, g, b = 0.0, 0.0, 0.0	# 펜 색상 초기화 (0,0,0)

## 프로그램 실행 ## 
turtle.title('거북이로 그림 그리기') # 프로그램 제목
turtle.shape('turtle') # 펜 커서 모양
turtle.pensize(pSize) # 펜 사이즈 

turtle.onscreenclick(screenLeftClick,1)	# 마우스 1번 (왼쪽) 클릭 시
turtle.onscreenclick(screenMidClick,2) # 마우스 2번 (휠) 클릭 시
turtle.onscreenclick(screenRightClick,3) # 마우스 3번 (오른쪽) 클릭 시 

turtle.done() # 프로그램 종료