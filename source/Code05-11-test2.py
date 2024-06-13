## 변수 선언 부분 ##
num = int(input("*** 숫자를 입력하세요 :"))
primeNum = True # 소수인지 아닌지 확인하는 boolean형 변수

# 실행 부분 
for i in range(2, num): # 2부터 num-1까지
    if num % i == 0 : # i로 나눠떨어지면
        primeNum = False # 소수가 아님

if primeNum :
    print("%d는 소수입니다." %num)
else : 
    print("%d는 소수가 아닙니다." %num)

