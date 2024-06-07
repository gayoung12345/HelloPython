dic = {} # dic이름을 가진 비어있는 딕셔너리 생성
dic['dictionary'] = '1. A reference book containing an ... '    # 딕셔너리명['key값'] = 'value값'
dic['python'] = 'Any of various nonvenomous snakes of the ... '
# 조회
print(dic['dictionary']) # 1. A reference book containing an ...

print()

smalldic = {'dictionary':'reference', 'python':'snake'} # 딕셔너리명 = {'key값':'value값'}
# 조회
print(smalldic['python']) # snake
print(smalldic) # {'dictionary': 'reference', 'python': 'snake'}
# 삭제
del smalldic['dictionary']
# 조회
print(smalldic) # {'python': 'snake'}

print()

# 딕셔너리 -> 리스트 
family = {'boy':'choi', 'girl':'kim', 'baby':'choi'}
print(family) # 값의 순서는 출력할 때 마다 다르게 나옴
print(family.keys()) # dict_keys(['boy', 'girl', 'baby'])
print(family.values()) # dict_values(['choi', 'kim', 'choi'])
#확인
print('boy' in family) # True
print('sister' in family) # False
