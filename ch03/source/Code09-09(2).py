## 함수 선언 부분 ##
def multi(v1, v2) :
     res1 = v1 + v2
     res2 = v1 - v2
     return res1, res2 # 두개의 변수를 리턴
	
## 전역 변수 선언 부분 ##
myList = []
hap, sub = 0, 0

## 메인 코드 부분 ##
hap, sub = multi(100, 200)
print("multi()에서 돌려준 값 ==> %d, %d" % (hap, sub))
