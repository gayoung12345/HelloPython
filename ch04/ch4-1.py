print(type(6))      # 6은 정수형. '<class 'int'>' 출력
print(type('A'))    # 'A'는 문자열 '<class 'str'>' 출력


# 1) 숫자
print(type(100000000))  # 정수 '<class 'int'>'출력
print(type(2.8))        # 부동소수점수(소수점 위치 고정X) '<class 'float'>'출력
print(type(3+4j))       # 복소수(숫자로 취급되는 식) '<class 'complex'>'출력


# 2) 시퀀스(str, list, tuple, user-defined class)
print(type("Love your Enemies, for they tell you your Faults."))    # 문자열 '<class 'str'>'출력
# 여러 개의 문자를 한 줄로 세워 둔 것이 문자열이므로, 문자열은 시퀀스이다.
print(type(['love', 'enemy', 'fault'])) # 리스트 '<class 'list'>'출력
print(type(('love', 'enemy', 'fault'))) # 튜플 '<class 'tuple'>'출력

# 문자열 슬라이싱 : 문자열 인덱스를 이용해서 문자열의 일부를 복사
p = 'Python'
print(p[0:2])   # Py        인덱스가 0부터 인덱스2 앞까지(즉, 인덱스1 까지)
print(p[:2])    # Py        시작 인덱스가 0이면 생략이 가능하다.
print(p[-2:])   # on        음수 인덱스를 사용해 뒷부분을 복사 (뒤에서 2번째 자리부터 0번째 앞 까지)
print(p[:])     # Python    앞뒤 숫자를 모두 생략하면 문자열 전체 복사
print(p[::-1])  # nohtyP    역순 복사


# 3) 매핑 : 딕셔너리(dict)가 키(key) + 값(value)으로 짝지어 이어진 것
print(type({'one':1, 'two':2, 'three':3})) # 매핑 '<class 'dict'>'출력
# 'one','two','three'는 key / 1,2,3은 value


# 4) 불 : 참, 거짓
print(type(False))          #        '<class 'bool'>'출력          
print(type(3 >= 1))         # 조건식 '<class 'bool'>'출력
print(type(True == 'True')) # 비교식 '<class 'bool'>'출력


# 5) 세트 : 원소의 순서가 유지되지 않고 중복 원소를 갖지 않음 (집합)
fruits = {'apple', 'banana', 'orange', 'apple'} 
print(fruits)   # apple은 한번만 출력되고, 출력되는 원소 순서는 실행할 때 마다 다름 
