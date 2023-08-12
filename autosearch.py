import pyautogui
import random
import string
import time

def random_mouse_movement():
    x_offset, y_offset = random.randint(-50, 50), random.randint(-50, 50)
    pyautogui.moveRel(x_offset, y_offset, duration=0.2)

def type_and_enter(word):
    pyautogui.typewrite(word, interval=0.1)
    pyautogui.press('enter')
    time.sleep(0.5)

def wait_for_page_to_load():
    time.sleep(4)

def close_and_open_tab():
    pyautogui.hotkey('ctrl', 'w')  
    time.sleep(0.5) 
    pyautogui.hotkey('ctrl', 't')  
    time.sleep(3)
def search_word_randomly(num_searches):
    for _ in range(num_searches):
      
        random_mouse_movement()
        search_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        type_and_enter(search_word)
        wait_for_page_to_load()
        close_and_open_tab()
num_searches = 20000
print("Place your cursor at the starting position and wait for 5 seconds...")
time.sleep(5)
start_x, start_y = pyautogui.position()
pyautogui.moveTo(start_x, start_y, duration=0.5)
search_word_randomly(num_searches)
