class Person:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    def eat(self):
        print('냠냠')
    
    def sleep(self):
        print('쿨쿨')

    def talk(self):
        print('주절주절')

class Student(Person): # Person class를 상속받음
    def study(self):
        print('열공')

# Person class로 만든 객체
lee = Person()
print(lee.mouth)
lee.talk()

# Student class로 만든 객체
kim = Student()
print(kim.mouth) 
kim.talk()
kim.study()