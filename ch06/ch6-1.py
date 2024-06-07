f = open(r'\HelloPython\ch06\fun.txt') # r'~' 원시문자열: 백슬래시를 해석하지 않는 문자열 리터럴
f.read() # 'Programming is fun.\nVery fun!\n\nYou have to do it yourself ...'

letter = open(r'\HelloPython\ch06\letter.txt','wt') # 'wr' 텍스트 파일을 쓰기 모드로 열기(기존의 내용을 삭제하고 그 위에서 씀=덮어쓰기)
letter.write('Dear Father,')    # 텍스트 문서에 들어갈 내용
letter.close() # 파일 닫기

letter = open(r'\HelloPython\ch06\letter.txt','a+') # 'a+' 텍스트 파일을 쓰기 모드로 열기(내용을 추가) 
letter.write('\n\nHow are you?')
letter.close()