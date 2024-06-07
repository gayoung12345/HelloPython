# set : 집합

fruits = {'apple', 'banana', 'orange'}
fruits.add('mango') # 추가
print(fruits) # {'banana', 'apple', 'orange', 'mango'}

companies = set() # 비어있는 세트 생성
companies = {'apple', 'microsoft', 'google'}
print(companies) # {'apple', 'google', 'microsoft'}

print(type(fruits)) # <class 'set'>
print(type(companies)) # <class 'set'>

print()

# 교집합
print(fruits & companies) # {'apple'}
# 합집합
print(fruits | companies) # {'orange', 'banana', 'microsoft', 'google', 'apple', 'mango'} 단, 중복되는 요소(apple)는 한번만 출력

print()

alphabet = list('google') 
print(alphabet) # ['g', 'o', 'o', 'g', 'l', 'e'] list는 순서를 가짐
print(set(alphabet)) # {'e', 'o', 'g', 'l'} # set는 순서를 가지지 않으며 중복 원소는 갖지 않는다

print()

# 집합끼리 연산 가능
S1 = {1, 2, 3, 4, 5, 6, 7}
S2 = {3, 6 ,9}
print(S1 - S2) # {1, 2, 4, 5, 7}