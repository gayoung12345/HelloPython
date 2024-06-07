#from datetime import datetime
#today = datetime.today()
#today

#def korean_age(year) :
#    return today.year - year + 1 

#print(korean_age(1997))

def korean_age(birth_year):
    # datetime 라이브러리 import
    from datetime import datetime
    # today 변수에 오늘 날짜 저장
    today = datetime.today()
    # 오늘 날짜 중 연도에서 생일 연도를 빼고 1을 더함 (한국식 나이)
    return today.year - birth_year + 1

# 출력
if __name__ == '__main__' :
    print("korean_age(2000): ", korean_age(2000))