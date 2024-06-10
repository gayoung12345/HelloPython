# method: class안에 있는 function. 객체.메소드()형식으로 호출

# 1) _init_ (초기화) : 어떤 클래스의 객체가 만들어질 때 자동으로 호출. 그 객체가 가질 여러가지 성질을 정의. 생성자의 역할
import bookstore
#b = bookstore.Book() # 책을 하나 출판했어요

#b.setData('누가 내 치즈를 먹었을까', '300원', '미키') # 입력
#b.printData() # 출력

b2 = bookstore.Book('내가 먹었지', '200d원', '미니') # 책을 하나 새로 출판했어요

print()

# 2) __del__ (소멸자) : 객체가 없어질 때 호출. 객체가 사라지기 전에 처리할 일이 있으면 사용

# 3) __repr__(프린팅) : 문자열을 return하면 print()를 사용하지 않아도 출력
b3 = bookstore.Book('나도 좀 줘', '100원', '쥐벼룩')
print(b3) # 책을 하나 새로 출판했어요 \n나도 좀 줘

print()

# 4) __add__(덧셈), __sub__(뺄셈) : 두개의 객체 self와 other를 인자를 받아 연산한 값을 return
import shape
a = shape.Shape()
a.area = 20
b = shape.Shape()
b.area = 10
print(a + b)
print(a.__sub__(b))

print()

# 3) __lt__(비교) : less than
c = shape.Shape()
c.area = 30
d = shape.Shape()
d.area = 20
print(c > d)
if c > d: print('c가 더 넓다')