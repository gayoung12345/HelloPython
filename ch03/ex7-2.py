def triple(x) :
    #return(x+x+x) 
    return x*3

print(triple(2))   # 6 출력
print(triple('x')) # xxx 출력

# 함수의 매개변수 타입에 따라 동작이 달라진다 : int형이면 *3(혹은 3번 더하기)이 연산, String형이면 해당 문자열이 3회 반복해서 출력됨