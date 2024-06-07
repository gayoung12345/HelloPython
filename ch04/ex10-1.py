# 함수 정의
def sumOfDisits(num) :
    # 지역변수 초기화
    num_list = []
    total = 0
    # 입력받은 문자열을 문자 하나씩 리스트에 복사
    for n in num:
        num_list.append(n)
    # 리스트에 저장된 문자열을 int형으로 바꾼 다음 누적 더하기
    for n in num_list:
        total += int(n)
    # 결과값 반환
    return total

# 실행부분
# 사용자에게 문자열을 입력받음
num = input('입력: ')
# 함수 호출 후 출력
print(sumOfDisits(num))


# Answer
def sumOfDigits2(num) :
    sum = 0
    for c in list(str(num)):
        sum += int(c)
    return sum

if __name__ == '__main__':
    print(sumOfDigits2(47253))
    print(sumOfDigits2(643))