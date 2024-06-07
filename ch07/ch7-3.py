# 1)class (diablo2.py)
#class Amazon:
#    strength = 20
#    dexterity = 25
#    vitality = 20
#    energy = 15

#    def attact(self):
#        return 'Jab!!!'

import diablo2
jane = diablo2.Amazon()
mary = diablo2.Amazon()

# diablo2 class에서 정의한 값 출력
print(jane.strength) # 20
print(jane.attact())

# 2) self (exercise() 추가)
    #def exercise(self):
        #self.strength += 2
        #self.dexterity += 3
        #self.vitality += 1

eve = diablo2.Amazon()
eve.exercise()
print(eve.strength) # 20