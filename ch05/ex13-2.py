# 피타고라스의 정의 a^ + b^ = c^
import math

# 1) a=3, b=4 일 때, c의 값 출력
print(math.sqrt(3**2 + 4**2))

# 2) 
def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return round(c,2) # round() : 소수점 이하의 값을 반올림하여 반환

print(hypotenuse(3, 4))
print(hypotenuse(10,20))