# 1)
def palindrome(str) :
    return str == str[::-1]

print(palindrome('anna'))      # True
print(palindrome('banana'))    # False

# 2)
def palindrome(str) :
    return str.lower() == str[::-1].lower()

print(palindrome('Anna'))   # True

# 3)
def palindrome(str) :
    return str.lower().replace(' ','') == str[::-1].lower().replace(' ','')
# ' '(공백O)을 ''(공백X)로 변경

print(palindrome('My gym'))   # True

### Answer ###

# 함수부분
def palindrome(s) :
    s = s.lower()
    s = s.replace(' ','')
    return s[:] == s[::-1]

# 실행부분
if __name__ == '__main__':
    for x in ['anna', 'banana', 'Anna', 'My gym']:
        if palindrome(x):
            print(f"'{x}' is a panlindrome")    # 회문이면 출력
        else: 
            print(f"'{x}' is not a panlindrome")    # 회문이 아니면 출력

# 입력값이 회문인지 테스트
str = input('문자열 입력: ')
print(palindrome(str))