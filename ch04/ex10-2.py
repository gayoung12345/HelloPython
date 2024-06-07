score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]
print(score)

stem_leaf = [[], [], []]

# 1)
for s in score :
    if(s>10) :
        d = s//10   # 10의 자리 (//: 정수 나눗셈(floor division))
        m = s%10    # 1의 자리
        stem_leaf[d].append(m)
    else :
        stem_leaf[0].append(s)

print(stem_leaf)

# 1) answer
#for s in score :
#    d, m = divmod(s, 10)    # divmod(): 두 개의 숫자를 인자로 받아 첫 번째 숫자를 두 번째 숫자로 나눈 몫과 나머지를 한 쌍으로 반환
#    stem_leaf[d].append(m)
#print(stem_leaf)

# 2) 틀린 풀이
#for d in stem_leaf:
#    for m in d:
#        print(f'{d[0]}:{m}')

# 2) answer
for i in range(len(stem_leaf)):
    print(f'{i}: {stem_leaf[i]}') # 자리수: 요소 출력
