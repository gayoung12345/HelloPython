class Fridge:
    def __init__(self):
        self.isOpened = False
        self.foods = []

    def open(self):
        self.isOpened = True
        print ('냉장고 문을 열다.')

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print('냉장고 속에 넣었다.')
        else:
            print('냉장고 문이 닫혀있어서 못 넣었다.')
    
    def close(self):
        self.isOpened = False
        print('냉장고 문을 닫다.')

class Food:
    pass