import pyautogui
import time

#print(pyautogui.size()) # 모니터 사이즈 출력

# 2초 뒤 마우스 위치 출력
#time.sleep(2) # 2초 기다림
#print(pyautogui.position()) # 마우스 좌표 출력 ( pyautogui.position().x , pyautogui.position().y )

# 한번에 이동
#pyautogui.moveTo(300, 200)
# 2초 만큼 이동
#pyautogui.moveTo(300, 200, 2)

# 왼쪽 클릭(기본값)
pyautogui.click()
# 더블 클릭
pyautogui.doubleClick()
# 오른쪽 클릭
pyautogui.click(button='right')
# 왼쪽 1초 마다 클릭 (3번)
pyautogui.click(clicks=3, interval=1)

# 왼쪽 드래그
pyautogui.drag(400, 500)
# 2초 동안 왼쪽 드래그
pyautogui.dragTo(400, 500, 2)
# 2초 동안 오른쪽 드래그
pyautogui.dragTo(400, 500, 2, button='right')