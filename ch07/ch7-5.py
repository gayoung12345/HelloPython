import fridge

# 냉장고 클래스 객체
f = fridge.Fridge()
# 음식 클래스 객체
apple = fridge.Food()
elephant = fridge.Food()

f.open() # 냉장고 문을 열다.
f.put(apple) # 냉장고 속에 넣었다.
f.put(elephant) # 냉장고 속에 넣었다.
print(f.foods) # [<fridge.Food object at 0x0000025F6F90ADB0>, <fridge.Food object at 0x0000025F6F90AF00>]
# f는 elephant를 가지고 있다 (has-a 관계)