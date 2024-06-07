# 1) calendar 모듈 impoert
import calendar
print("1)")
print(dir(calendar)) # calendar 모듈의 directory 확인

# 2) calendar모듈에 leap라는 문자열을 포함 하는 것의 이름 확인
print("2)")
print([x for x in dir(calendar) if 'leap' in x]) # ['isleap', 'leapdays']
# list comprehension : 반복문과 조건문을 한 줄에 표현하여 리스트
# [표현식(항목에 적용될 표현식) for 항목(interable에서 가져온 항목) in 반복가능객체(interable:list,tuple,..) if 조건]

# 3) 윤년(leap)인지 아닌지 판별하는 함수의 사용법 확인
print("3)")
help(calendar.isleap)

# 4) isleap()를 사용해서 2077년이 윤년인지 아닌지 확인
print("4)")
print(calendar.isleap(2077)) # False