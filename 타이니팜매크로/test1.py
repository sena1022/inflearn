import pyautogui as pag
import random, time, subprocess
import mss, cv2
import numpy as np
from datetime import datetime

from imagesearch import *  #https://github.com/drov0/python-imagesearch


def logout() :
    search_move("2_logout1.png")
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))

    run()

    search_click("2_logout2.png")
    time.sleep(random.uniform(1.05001, 1.79987))
    search_click("2_logout3.png")
    time.sleep(random.uniform(1.55001, 2.79987))
    #터틀맵 입장

    run()

    search_move("2_logout4.png")
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)

    run()

    search_move("2_logout5.png")
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    search_click("2_logout6.png")
    time.sleep(random.uniform(0.05001, 0.19987))





def search_move(img):
    duration=random.uniform(0.3, 0.7)
    pos = imagesearch(img)
    if pos[0] != -1:
        time.sleep(r(0.1, 0.2))
        img = cv2.imread(img)
        height, width, channels = img.shape
        offset = min(height, width)
        pyautogui.moveTo(pos[0] + r(width, -offset), pos[1] + r(height, -offset),
                         duration)



def search_click(img, action='left'):
    duration=random.uniform(0.3, 0.7)
    pos = imagesearch(img)
    if pos[0] != -1:
        time.sleep(r(0.1, 0.2))
        img = cv2.imread(img)
        height, width, channels = img.shape
        offset = min(height, width)
        pyautogui.moveTo(pos[0] + r(width, -offset), pos[1] + r(height, -offset),
                         duration)
        time.sleep(random.uniform(0.01, 0.3))
        pyautogui.click(button=action)



#마우스 클릭
def mouse_click(top_x, top_y, bottom_x, bottom_y) :
    login_button = {
        'top_left': {
            'x': a,
            'y': b
        },
        'bottom_right': {
            'x': c,
            'y': d
        }
    }
    pag.moveTo(
        x = random.uniform(login_button['top_left']['x'], login_button['bottom_right']['x']),
        y = random.uniform(login_button['top_left']['y'], login_button['bottom_right']['y']),
        duration=random.uniform(0.5, 1.5)
    )



def mouse_scroll(m_scroll) :
    pyautogui.scroll(m_scroll) #위로 위로 위로위로
    # pyautogui.scroll(-200) #아래로 내림



def login(id, pw) :
    search_click('1_login4.png')
    search_click('1_login4.png')                       #logout
    time.sleep(random.uniform(2.5001, 3.9987))
    search_click('1_login1.png')                       #id 입력
    time.sleep(random.uniform(0.15001, 0.29987))
    pyautogui.press('end')
    time.sleep(random.uniform(0.15001, 0.29987))
    #backspace 7번
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.05001, 0.19987))
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.05001, 0.19987))
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.05001, 0.19987))
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.05001, 0.19987))
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.05001, 0.19987))
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.05001, 0.19987))
    pyautogui.press('backspace')
    time.sleep(random.uniform(0.05001, 0.19987))
    # pyautogui.press('backspace')
    pyautogui.typewrite(id, random.uniform(0.30001, 0.69999)) #한글 입력은 안 됨
    time.sleep(random.uniform(0.05001, 0.19987))
    pyautogui.press('tab')                           #pw 입력
    time.sleep(random.uniform(0.05001, 0.19987))
    pyautogui.typewrite(pw, random.uniform(0.30001, 0.69999))
    # pyautogui.press('tab')
    # pyautogui.press('Enter')
    search_click('1_login2.png')
    time.sleep(random.uniform(2.5001, 3.9987))
    search_click('1_login3.png')


def first() :
    presence = imagesearch("3_first1.png")
    if (presence[0] != -1) :
        search_click("3_first1.png")
        time.sleep(random.uniform(1.05001, 1.79987))
        search_click("3_first2.png")
        time.sleep(random.uniform(1.05001, 1.79987))
        search_click("3_first3.png")
        time.sleep(random.uniform(1.05001, 1.79987))
        search_click("3_first4.png")
        time.sleep(random.uniform(1.05001, 1.79987))




def run_bell() :
    max_retries = 2
    retries  = 0
    while True:
        if retries >= max_retries:
            time.sleep(random.uniform(0.80001, 1.89999))
            break
        presence = imagesearch("5_food1.png")
        if (presence[0] == -1):
            retries += 1
            continue
        else :
            search_click("4_building_bell.png")
            search_click("4_building_bell2.png")
            search_click("4_building_love.png")
            search_click("4_building_love2.png")
            continue


def run() :
    max_retries = 4
    retries  = 0
    while True:
        if retries >= max_retries:
            time.sleep(random.uniform(0.80001, 1.89999))
            break
        presence = imagesearch("5_food1.png")
        if (presence[0] == -1):
            retries += 1
            continue
        else :
            search_click("4_building2.png")

            search_click("5_food1.png")

            search_click("friend1.png")
            search_click("friend2.png")
            search_click("friend3.png")

            search_click("2_logout4_building1.png")
            continue



def main():
    # login('agnus8', '1022')
    # time.sleep(random.uniform(8.55001, 10.79987))
    # first()
    run_bell()
    run()
    logout()



if __name__ == '__main__':
    main()


#3 완료
