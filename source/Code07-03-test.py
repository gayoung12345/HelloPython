aa = []
for i in range(0, 10) :
    aa.append(0)
hap = 0

for i in range(0, 10) :
    aa[i] = int(input(str(i+1) + "번째 숫자 : " ))

cnt = 0
hap = 0
while cnt <10 :
    hap = hap + aa[cnt]
    cnt = cnt + 1

print("합계 ==> %d" % hap)
