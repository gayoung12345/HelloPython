## 함수 선언 부분 ##
def calc(v1, v2, op) :
     result = 0

     if op == '+' :
          result = v1 + v2
     elif op == '-' :
          result = v1 - v2
     elif op == '*' :
          result = v1 * v2
     elif op == '/' :
          if v2 == 0 :
               print('0으로는 나눌 수 없습니다.')
               return
          result = v1 / v2
     elif op == '**':
          result = v1 ** v2
	
     return result

## 전역 변수 선언 부분 ##
res = 0
var1, var2, oper = 0, 0, ""

## 메인 코드 부분 ##
var1 = int(input("첫 번째 수를 입력하세요 : "))
oper = input("계산을 입력하세요(+, -, *, /, **) : ")
var2 = int(input("두 번째 수를 입력하세요 : "))

res = calc(var1, var2, oper)

if res is not None: # calc()결과가 None이 아니면(계산이 성공하면) 아래 코드 실행
     print("## 계산기 : %d %s %d = %d" % (var1, oper, var2, res))
