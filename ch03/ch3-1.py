a_list = [3, 4 ,62, 27, 83, 956, 26, 58, 3, 78, 168, 64, 78] # a_list 정의

# len():리스트에 들어있는 원소 개수(즉, 리스트의 크기)를 반환
len([1, 2, 3, 4, 5]) # 리스트를 따로 정의하지 않고 함수 안에 넣어서도 사용이 가능하다.
len(a_list) # 미리 정의한 리스트를 파라미터로 넣어서도 사용이 가능하다.

# 함수 정의
def print_list(a):  # a는 리스트
    for x in a: # x번째 자리에 있는 a리스트 원소를 출력한다 (x는 0 ~ a.length)
        print(x)

# 매개변수가 없는 함수
def boy():
    print('I am a boy.')
    print('You are a girl.')

# a,b비교 함수
def print_abCompare(x, y):
    if x>y:
        print('a>b')
    elif x<y:
        print('a<b')
    elif x==y:
        print('a=b')
    else :
        ('i dont know')
