dice1 = {1, 2, 3, 4, 5, 6}
dice2 = {2, 3, 5, 7, 11, 13}

sum_of_the_two_dice = set() # set이므로 중복요소는 저장하지 않음
for x in dice1:
    for y in dice2:
        sum_of_the_two_dice.add(x + y) # 2중 for문으로 두 개의 주사위 눈금을 더한 값을 set()에 저장
# 출력
print(sum_of_the_two_dice) 