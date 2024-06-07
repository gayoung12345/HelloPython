import glob

outfile = open("out.txt", "wt") # 파일 열기

for x in glob.glob("korean_national_anthem_?.txt"): # korean_national_anthem_?.txt와 같은 이름 패턴을 가진 파일을 찾기
    # infile = open(x, "rt") # encoding에러 발생
    infile = open(x, "rt", encoding="utf-8-sig") # rt모드로 열기
    outfile.write(x + '\n') # 파일제목 적기 
    outfile.write('-' * len(x) + '\n')  # 구분선 적기
    outfile.write(infile.read()+"\n\n") # 파일내용 적기

outfile.close() # 파일 닫기