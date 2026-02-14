import pyautogui
import keyboard as keyboard_lib

print('digite h para iniciar o programa')
keyboard_lib.wait('h')
print('digite x para encerrar o programa')

while not keyboard_lib.is_pressed('x'):
    pyautogui.click()
