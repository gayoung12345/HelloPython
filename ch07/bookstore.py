class Book:

    # 자료 입력
    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
    
    # 자료 출력
    def printData(self):
        print('제목: ', self.title)
        print('가격: ', self.price)
        print('저자: ', self.author)

    # 초기화 메소드
    #def __init__(self):
    #    print('책을 하나 출판했어요')
    def __init__(self, title, price, author):
        self.setData(title, price, author)
        print('책을 하나 새로 출판했어요')

    # 프린트
    def __repr__(self):
        return self.title