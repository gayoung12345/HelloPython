# 프렉탈 규칙
rule90={'000':'0', '001':'1', '010':'0', '011':'1', '100':'1', '101':'0', '110':'1', '111':'0'} 
# 가로세로 길이 
colwidth = 79
# 줄의 절반
half = colwidth // 2 # 79/2 = 39.5 이므로 소수점 자리를 버리고 39
line = '0' * half + '1' + '0' * half # 첫번째 줄
print(line) # 첫번째 줄 출력
# 두번째 줄 부터 마지막 줄 까지 출력
while line[1] == '0':   # line의 index가 1이(두번째 칸이) '1'이 되면 실행 종료
    prev = line # 이전 줄의 상태를 저장
    line = '0' * colwidth
    for i in range(1, colwidth-1) : # 가장 왼쪽과 가장 오른쪽에 있는 셀은 규칙에 따라 이웃하는 두 셀의 상태가 필요
        line = line[:i] + rule90[prev[i-1:i+2]] + line[i+1:]
    print(line)
