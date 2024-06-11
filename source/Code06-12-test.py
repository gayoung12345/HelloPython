hap = 0
a, b = 0, 0

while True :
     a = input("더할 첫 번째 수를 입력하세요 : ")
     if a == '$' :
          print("$을 입력해 반복문을 탈출했습니다")
          break
     b = input("더할 두 번째 수를 입력하세요 : ")
     if b == '$' :
          print("$을 입력해 반복문을 탈출했습니다")
          break
     hap = int(a) + int(b)
     print("%s + %s = %d" % (a, b, hap))


