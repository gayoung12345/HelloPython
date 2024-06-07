## 함수 선언 부분 ##
def multi(v1, v2) :
     retList=[]       # 반환할 리스트
     res1 = v1 + v2
     res2 = v1 - v2
     retList.append(res1)     # append()리스트에 데이터 추가
     retList.append(res2)
     return retList # 여러개의 값이 담긴 리스트를 리턴
	
## 전역 변수 선언 부분 ##
myList = []
hap, sub = 0, 0

## 메인 코드 부분 ##
myList = multi(100, 200)
hap = myList[0]
sub = myList[1]
print("multi()에서 돌려준 값 ==> %d, %d" % (hap, sub))
