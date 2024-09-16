import pyautogui
import keyboard
from time import sleep

# Link para o jogo: https://guitarflash.com/?lg=pt
# 1- verificar se há uma cor correspondente a cor do círculo

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(825,552,(12,152,33)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(915,552,(247,44,2)): 
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1003,552,(244,244,31)):  
        pyautogui.press('j')  
        sleep(0.05)  