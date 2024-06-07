# year = int(input('연도입력: '))

# if year%4 == 0 :
#    if year%100 == 0 :
#        if year%400 == 0 :
#            print('윤년입니다.')
#        else: 
#            print('윤년이 아닙니다')
#    else: 
#        print('윤년입니다.')
# else: 
#    print('윤년이 아닙니다')

while True :
    is_leap_year = None
    year = int(input())
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
            else: 
                is_leap_year = False
        else :
            is_leap_year = True
    else :
        is_leap_year = False
    if is_leap_year :
        print(f'{year} is a leap year')
    else :
        print(f'{year} is not a leap year')        