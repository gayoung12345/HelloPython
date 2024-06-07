# 1) 전체 파일 읽어오기
txt = open("C:\HelloPython\ch06\postcard.txt", "r").read()
print("*** 1. Full Text ***\n" + txt + '\n')

# 2) 엽서의 머리말, 본문, 꼬리말 중에 본문만 읽어오기
head, body, tail = tuple(txt.split('\n\n')) # 두 번 줄 바꿨는지를 기준으로 tuple생성 
print("*** 2. Body *** \n" + body + '\n')

# 3) 문장 부호 제거
import re # 정규 표현식(regular expression) 제공 모듈
s = re.sub('[:,\.]', '', body)  # sub(바꿀 문자열, 대체 문자열, 제공된 문자열)
                                # [:,\.] 은 정규 표현식 패턴으로 작성되었고 쉼표(,), 콜론(:), 마침표(.) 중에 하나 라는 의미
print("*** 3. Text without Punctuation *** \n" + s  + '\n')

# 4) 대문자로 변환
s = s.upper()
print(("*** 4. Uppercase *** \n " + s  + '\n'))

# 5) 각 행의 처음 두 단어만 추려서 출력
secret_words = []   # 빈 리스트 정의
for line in s.split('\n'):  # 문자열 s가 \n 될 때를 기준으로 분할
    secret_words += line.split()[:2] # line의 0에서 1까지(2앞까지) 문자를 secret_words에 저장

message = ' '.join(secret_words) # secret_words리스트에 있는 원소들을 공백으로 연결해서 message에 저장
print("*** 5. Secret Message *** \n " + message + '\n')

# 만약 따로 join을 하지 않았을 경우 리스트 형태로 출력
print (secret_words)