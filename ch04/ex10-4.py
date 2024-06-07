print("진법 전환 예시")
print(divmod(13, 2))    # (6, 1) 몫, 나머지
print(divmod(6, 2))     # (3, 0)
print(divmod(3, 2))     # (1, 1)
print(divmod(1, 2))     # (0, 1)
print(bin(13))          # 0b 1101 이진수
print()

# 문제 풀이
# 변수 선언
num = int(input('입력: '))
num_list = []
x , y = 1, 0
# while문
while(x != 0):
    x,y = divmod(num,2)
    num_list.append(y)
    num = x
# 출력
print(num_list[::-1])


# answer

#d = int(input())
#m = d
#b = []

#while True:
#    d, m = divmod(d, 2)
#    b.insert(0, m)
#    if d == 0:
#        break
#print(b)