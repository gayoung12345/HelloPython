## 변수 선언 부분 ##
num1 = int(input("*** 첫 번째 숫자를 입력하세요 :"))
num2 = int(input("*** 두 번째 숫자를 입력하세요 :"))
addValue = int(input("*** 더할 숫자를 입력하세요 : "))
result = 0

# 실행 부분
for i in range(num1, num2+1, addValue) : # range(시작값, 끝값+1, 증가값)
        result = result + i
print("%d+%d+...+%d는 %d입니다. " %(num1, num1+addValue, num2, result))

