def multi(m):
    for n in range(1, 10):
        print(f'{m} * {n} = {m*n:2d}')

#for i in range(2,10) :
#    print(f'{i}단')
#    multi(i)
#    print()

if __name__ == '__main__':
    for i in range(2, 10):  # 범위: 2~9까지
        multi(i)    # 함수 호출
        print()