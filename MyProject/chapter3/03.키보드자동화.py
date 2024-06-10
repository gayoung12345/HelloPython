import pyautogui

# 1. 키보드 입력(문자)
#pyautogui.write('startcoding') 
#pyautogui.write('startcoding', interval=0.25) # 타이핑 간격 0.25초
#pyautogui.write('스타트코딩') # 한글 지원X

# 2. 키보드 입력(키) : enter, space, bar, ↑, ↓, ←, →
#pyautogui.press('enter') # press(): key down + key up
#pyautogui.press('up')

# 3-1. 키보드 다중 입력 (ctrl+c)
#pyautogui.keyDown('ctrl')
#pyautogui.press('c')
#pyautogui.keyUp('ctrl')

# 3-2. hotkey 이용
#pyautogui.hotkey('ctrl','c')

# 4. 한글 입력 방법
import pyperclip

pyperclip.copy('스타트코딩') # 한글 복사
pyautogui.hotkey('ctrl','v') # 붙여넣기