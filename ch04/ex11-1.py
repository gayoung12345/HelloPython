def korean_number(num) :
    numbers = {0:'영',1:'일',2:'이',3:'삼',4:'사',5:'오',6:'육',7:'칠',8:'팔',9:'구'}
    return numbers[num]

print(korean_number(3))
print(korean_number(6))
print(korean_number(9))