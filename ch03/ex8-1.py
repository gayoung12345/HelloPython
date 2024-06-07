# 이자(interest) = 원금(principal) * 이율(rate) * 기간(time)
# 원리금(Amount) = 원금(principal) + 이자(interest) = 원금(principal) * (1 + 이율(rate) * 기간(time))

# 이자를 구하는 함수
def simple_interest(p, r, t) :
    print(p * r * t)
    return p * r * t

simple_interest(10000000, 0.03875, 5)
simple_interest(1100000,0.05,5/12)

# 원리금을 구하는 함수
def simple_interest_amount(p, r, t) :
    #print(p + p * r * t)
    #return p + p * r * t
    print(p * (1 + r * t))
    return p * (1 + r * t)

simple_interest_amount(10000000, 0.03875, 5)
simple_interest_amount(1100000,0.05,5/12)

