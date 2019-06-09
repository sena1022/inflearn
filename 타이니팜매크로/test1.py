import pyautogui as pag
import random, time, subprocess
import mss, cv2
import numpy as np
from datetime import datetime

from imagesearch import *  #https://github.com/drov0/python-imagesearch


def logout() :
    mouse_click(800, 350, 840, 420)
    # search_move("2_logout1.png")
    # time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))

    run()

    search_click("2_logout2.png")
    time.sleep(random.uniform(1.05001, 1.79987))

    pos = imagesearch("2_logout3.png")
    if pos[0] != -1:
        search_click("2_logout3.png")
        time.sleep(random.uniform(1.55001, 2.79987))
    else :
        print("somethine wrong~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #터틀맵 입장
    run()
    mouse_click(800, 350, 840, 420)
    # search_move("2_logout4.png")
    # time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    run()
    mouse_click(20, 200, 70, 310)
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
        time.sleep(random.uniform(0.01, 0.3))
        img = cv2.imread(img)
        height, width, channels = img.shape
        offset = min(height, width)
        pyautogui.moveTo(pos[0] + r(width, -offset), pos[1] + r(height, -offset),
                         duration)
        time.sleep(random.uniform(0.01, 0.3))
        pyautogui.click(button=action)


# x: 100              y : 70
# x: 750              y : 420
def search_click_range(img, action='left'):
    duration=random.uniform(0.3, 0.7)
    pos = imagesearch(img)
    print(pos[0], pos[1])
    if pos[0] != -1:
        if pos[0]>= 100 and pos[0] < 750 and pos[1] >= 70 and pos[1] < 420 :
            time.sleep(random.uniform(0.01, 0.3))
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
            'x': top_x,
            'y': top_y
        },
        'bottom_right': {
            'x': bottom_x,
            'y': bottom_y
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
    time.sleep(random.uniform(0.05001, 0.19987))
    search_click('1_login4.png')                       #logout
    time.sleep(random.uniform(2.5001, 3.9987))

    #id 입력
    search_click('1_login1.png')
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
    pos = imagesearch("1_login3.png")
    if pos[0] != -1:
        search_click("1_login3.png")
        time.sleep(random.uniform(1.55001, 2.79987))
    else :
        print("somethine wrong~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




def first() :
    max_retries = 2
    retries  = 0
    while True:
        if retries >= max_retries:
            break
        time.sleep(random.uniform(3.55001, 5.79987))
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
        else :
            retries += 1
            continue




def run_bell() :
    max_retries = 2
    retries  = 0
    while True:
        if retries >= max_retries:
            time.sleep(random.uniform(0.80001, 1.89999))
            break
        # presence = imagesearch("5_food1.png")
        # if (presence[0] != -1):
        search_click("4_building_bell.png")
        search_click("4_building_bell2.png")
        search_click("4_building_love.png")
        search_click("4_building_love2.png")
            # continue
        # else :
        retries += 1
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
            search_click_range("4_building2.png")

            search_click_range("5_food1.png")

            search_click_range("friend1.png")
            search_click_range("friend2.png")
            search_click_range("friend3.png")

            search_click_range("2_logout4_building1.png")
            continue



def main():
    # login('agnus0', '1022')
    # first()
    # run_bell()
    run()
    logout()



if __name__ == '__main__':
    main()


#3 완료
