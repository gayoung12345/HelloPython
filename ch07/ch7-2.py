class Singer:
    # class가 하는 행동 정의
    def sing(self):
        return "Lalala~"

# 객체1 = class()로 만듬
iu = Singer()
# 객체.메소드
print(iu.sing()) # Lalala~

# 객체2
bruno = Singer()
print(bruno.sing()) # Lalala~
