def f1(x):
    a = 3
    b = 5
    y = a * x + b
    return y    # y값 반환

c = f1(10)  # c = 35
print(c)    # 35 출력

def f2(x):
    a = 3
    b = 5
    y = a * x + b
    print(y)    # 반환 하는 값 없이 y의 값을 출력
                # 반환 구문이 없는 함수는 None을 반환

d = f2(10)  # 함수 호출되므로 35가 출력
print(d)    # None 출력

# 삼각형의 넓이를 구하는 함수
def triangle(x, y): # x,y: 밑변, 높이
    return x*y/2    # (밑변 *높이)/2

1 + 1 == 2 # True 출력
1 + 1 == 3 # False 출력

if 1 + 1 == 2 :
    print('yes')
else : 
    print('no')
# yes 출력

def quiz():
    ans = input('1 + 2 = ')     # 사용자에게 입력받은 문자열을 ans에 저장
    return 1 + 2 == int(ans)    # int(ans)로 문자열을 int형으로 변환하고 1+2연산 결과 값과 비교
                                # 결과 값과 사용자 입력 값이 같으면 True, 틀리면 False 출력
quit() # 1 + 2 = 가 출력 되고 사용자에게 문자열을 입력 받음
