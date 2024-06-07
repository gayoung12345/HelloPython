# 복리(compound interest)예금에 대한 원리금 = 원금(principal) * (1 + 연이율(rate) / 복리 횟수(number)) ** (복리 횟수(number) * 기간(time))

# 복리 예금에 대한 원리금(복리이자 + 원금)을 구하는 함수
def compound_interest(p, r, t, n) :
    return p * (1 + r / n ) ** (n*t) # **연산자: 앞의 항을 뒤에 항의 수 만큼 거듭제곱

print(compound_interest(1500000, 0.043,6,4))