favorite = 'apple'
favorite = 'orange'
print(f'favorite = {favorite}') # orange출력

def new():
    favorite = 'apple mango'
    print(f'favorite = {favorite}')

new() # 함수호출, apple mango 출력

print(f'favorite = {favorite}') # orange출력

# => new() 안에 있는 favorite은 지역변수이므로 이런 결과가 나옴

def d_is_10():
    d = 10 #지역변수
    print (f'd 값은 {d}입니다.')

d_is_10() # 함수호출, 'd 값은 10입니다.' 출력
# 함수 실행 후 d 삭제
# print(d)  # 실행하면 defined에러 발생
            # d는 지역변수이므로 함수를 벗어나면 소멸됨
            # 함수 호출 후, 함수가 종료되면 메모리에서 삭제됨

x = 10 # 전역변수
def print_x() :
    print(x)

print_x() # 함수호출, '10' 출력
# x는 전역변수이므로 함수 실행이 종료되어도 삭제 되지 않고 메모리에 남아있음
print(x) # 10 출력

def e_is_10():
    global e # e는 함수 안에서 선언되었지만 global 표기를 사용했으므로 전역변수 
    e = 10
    print (f'e 값은 {e}입니다.')

e_is_10() # 함수호출, 'e 값은 10입니다.' 출력
# e는 전역변수 표기가 되어 있으므로, 함수 실행이 종료되어도 삭제 되지 않고 메모리에 남아있음
print(e) # 10 출력


