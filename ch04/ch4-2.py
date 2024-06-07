# 1) 문자열: 한 글자마다 index 번호를 지정

x = 'banana'    
print(x[0])     # 0번째 위치한 글자 'b'출력
print(x[2:4])   # 2번째 ~ 3번째(4번째 앞)까지 글자 'na'출력
print(x[:3])    # 0번째 ~ 2번째(3번째 앞)까지 글자 'ban'출력
print(x[3:])    # 3번째 ~ 끝까지 글자 'ana'출력

print()

# x의 첫번째 글자를 'n'으로 변경하는 법
# x[0] = 'n' # typeError 발생()
x = 'n' + x[1:] # x = n + anana (즉, b를 n으로 변경한 것이 아니다) 
print(x)

print()

# find(): 글자의 위치를 찾는 함수
s = "hello Python!"
print(s.find('P')) # 해당 문자열의 7번째 자리(공백 포함)에 위치하므로 index 번호인 6 출력

print()

# slicing: 시퀀스 객체에 범위를 지정해서 객체를 가져옴
print(s[0:6]) # 'hello '의 위치 확인
h = s[0:6] # 변수 h에 변수s의 0번째~5번째(6번째 앞)까지 문자열을 복사
print(h) # 'hello ' 복사 완료

print()

# rstrip():공백제거 함수
print(len(h[0:5])) # 5 출력(마지막에 공백이 없음) 문자열h의 공백을 삭제 한 것이 아니라, 공백 앞 까지만 출력 한 것임 
print(len(h.rstrip())) # 5 출력
print(len(h)) # 6 출력 

print()

# split(): 주어진 문자열을 분할한 리스트 생성
print(s.split()) # ['hello', 'Python!'] 출력
print(s.split()[0]) # s.split리스트의 0번째 자리에 있는 'hello' 출력 

print()

# 2) 리스트

# append(): 리스트의 마지막에 원소 추가 함수
prime = [3, 7, 11] # 3, 7, 11으르 원소로 갖는 리스트 prime을 만듦
prime.append(5) # prime에 원소 5를 추가
print(prime) # [3, 7, 11, 5]

print()

# sort(): 리스트의 원소를 크기순으로 정렬
prime.sort()
print(prime) # [3, 5, 7, 11]

print()

# insert(): 리스트의 지정 위치에 원소 추가 함수
prime.insert(0, 2) # prime 리스트의 0번째 자리에 2를 삽입
print(prime) # [2, 3, 5, 7, 11]

print()

# del: 원소 삭제
del prime[4] # prime의 4번 원소(11)를 삭제
print(prime) # [2, 3, 5, 7]

print()

# pop(): 리스트에서 해당 원소를 삭제하고 삭제한 원소를 반환(return)
a = prime.pop() # 리스트의 가장 마지막 원소를 삭제하고, 삭제한 원소를 a변수로 받음
print(prime) # [2, 3, 5]
print(a) # 7

print()

# 리스트의 원소에 새로운 값 지정 
prime[0] = 1
print(prime) # [1, 3, 5]

print()

# 리스트 안 리스트(이중리스트)
orders = ['potato', ['pizza', 'coke', 'salad'], 'hamburger']
print(orders[1]) # ['pizza', 'coke', 'salad']
print(orders[1][2]) # salad

print()

# 리스트로 행렬 표현
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print()

# 3)문자열을 리스트로 바꾸기 

characters = [] # 리스트
sentence = 'Be happy!'  # 문자열
for char in sentence:
    characters.append(char) # 문자열을 리스트로 추가(append)

print(characters) # ['B', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '!']
print(list('Be happy!')) # ['B', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '!'] # 문자열을 리스트로 바로 변환

print()

# 4) 숫자를 문자열로 바꾸기 
my_int = 123
print(type(my_int)) # <class 'int'>
print(type(str(my_int))) # <class 'str'> int형을 str형으로 변환
my_str = str(my_int) # int형으로 str형을 얻어 새로운 변수에 할당

print()

# 5) 문자열을 숫자로 바꾸기
print(type(int('123'))) # <class 'int'>
print(type(float('123'))) # <class 'float'>

print()

# 6) 리스트 원소들의 합 구하기
one_to_ten = list(range(1, 11)) # 리스트 생성
print(one_to_ten) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum(): 리스트의 모든 값을 더함
print(sum(one_to_ten)) # 55

print()

# 7) 리스트를 응용하여 성적표 만들기

# 학생 = [국어, 영어, 수학]
chulsu = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 60, 70]
# 학생 리스트에 학생들을 넣어줌
students = [chulsu, younghee, yong, minsu] 
# 학생 점수를 출력하는 함수
def print_scores ():
    for scores in students:
        print(scores)
# 함수 호출
print_scores()
print()
# 총점과 평균을 출력하는 함수
def print_total_average () :
    for scores in students:
        total = 0
        for s in scores:
            total = total + s
        average = total / 3
        print(scores, total, average)
# 함수 호출
print_total_average() # 학생점수리스트, 총점, 평균