## 변수 선언 부분 ##
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0 # 값 초기화

## 메인 코드 부분 ##
money=int(input("교환할 돈은 얼마 ? "))

c50000 = money // 50000 # 50000원 짜리 지폐 개수 구함
money %= 50000 # 나머지 값 저장

c10000 = money // 10000 # 10000원 짜리 지폐 개수 구함
money %= 10000 # 나머지 값 저장

c5000 = money // 5000 # 5000원 짜리 지폐 개수 구함
money %= 5000 # 나머지 값 저장

c1000 = money // 1000 # 1000원짜리 지폐 개수 구함
money %= 1000 # 나머지 값 저장(바꾸지 못한 남은 잔돈)

print("\n 50000원짜리 ==> %d장" % c50000)
print(" 10000원짜리   ==> %d장" % c10000)
print(" 5000원짜리 ==> %d장" % c5000)
print(" 1000원짜리   ==> %d장" % c1000)
print(" 바꾸지 못한 잔돈 ==> %d원" % money) # 10 미만
