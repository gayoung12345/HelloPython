L = list(range(2, 11)) # 찾고자 하는 범위의 자연수를 나열
print(L) # [2, 3, 4, 5, 6, 7, 8, 9, 10]
L.remove(4); L.remove(6); L.remove(8); L.remove(10) # 2의 배수 삭제
L.remove(9) # 3의 배수 삭제
print(L) # [2, 3, 5, 7]

# 답지 1번
def answer1(num) :
    userList = list(range(2,num+1)) # 리스트 생성
    primeList = userList[:] # 새로운 리스트에 복사

    for p in userList :
        for q in userList:
            if(q in primeList) and (q != p and q % p == 0): # 복사한 리스트에 있으면서 본인이 아닌 수로 나눠지는 수(소수가 아님)
                primeList.remove(q) # 삭제
    print(primeList) # 소수만 남음

num = int(input('입력: '))
answer1(num)