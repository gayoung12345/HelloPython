def f(a, b):
    try: # 시도
        if a and b: # a 와 b가 둘 다 0이 아닐 때
            return (a * b) + (a / b)
        elif a: # a만 0이 아닐 때 (b = 0)
            return '불능'
        else: # 둘 다 0 일 때
            return '부정'
    except: # 예외 발생 시
        return '예외처리'