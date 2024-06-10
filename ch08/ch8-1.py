# print 안녕 # SyntaxError

def f(a, b): 
    return (a * b) + (a / b)
# f(3, 0) # ZeroDivisionError

def f(a, b):
    if a and b: # a 와 b가 둘 다 0이 아닐 때
        return (a * b) + (a / b)
    elif a: # a만 0이 아닐 때 (b = 0)
        return '불능'
    else: # 둘 다 0 일 때
        return '부정'
f(3,0)
f(0,0)

# f(이십,오) # NameError
