
import pyautogui
import time

#descobir cordenadas do mouse
"""currentMouseX, currentMouseY = pyautogui.position()
time.sleep(5)
print("x=",currentMouseX, "y=", currentMouseY)"""

#abrindo google drive com nagevador Brave
pyautogui.press('Winleft')
pyautogui.write('Brave')
pyautogui.press('Enter')
time.sleep(2)
pyautogui.write('https://drive.google.com/drive/u/3/folders/1NExrQs_yv8hxSdiEJwShFOySEOKwOGzo')
pyautogui.press('Enter')
time.sleep(2)

pyautogui.press('Winleft')
pyautogui.write('Explorador de Arquivos')
time.sleep(2)
pyautogui.press('Enter')
time.sleep(2)
pyautogui.write('Documentos')
pyautogui.press('Enter')
time.sleep(2)
pyautogui.write('Python projects')
pyautogui.press('Enter')
pyautogui.write('automatization-horario')
pyautogui.press('Enter')

"""ainda estou estudando uma maneira de clicar no arquivo e arrastar para o drive
pois, hora abre o explorer full janela hora não"""


