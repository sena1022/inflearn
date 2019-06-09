import pyautogui as pag
import random, time, subprocess
import mss, cv2
import numpy as np
from datetime import datetime

from imagesearch import *  #https://github.com/drov0/python-imagesearch






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
    # print(pos[0], pos[1])
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
def mouse_move(top_x, top_y, bottom_x, bottom_y) :
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



def first() :   #로그인시 클릭해야할것들 1
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

            run_bell()
            # Q_hunt_1()
            # Q_animal()
            # Q_luckybag()
            # Q_safari()
            # Q_village()
            #
            # run()
            #
            # mouse_move(800, 350, 840, 420)
            # mouse_scroll(-1)
            # time.sleep(random.uniform(0.60001, 1.09999))
            #
            # run()
            #
            # Q_friend()
            # Q_hunt_2()


        else :
            retries += 1
            continue



def run_bell() :  #벨트리, 러브하우스 클릭
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



def run() :  #클릭하기
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



def Q_hunt_1() :    #6모험가 확인
    search_click("Q_hunt_1_1.png")

def Q_hunt_2() :    #6모험가 모헙 보내기
    search_click("4_building_bell.png")

def Q_animal() :    #7교배소
    search_click("4_building_bell.png")

def Q_luckybag() :  #8럭키백
    search_click("4_building_bell.png")

def Q_safari() :    #9사파리
    search_click("4_building_bell.png")

def Q_village() :    #10마을 출석, 애정환원
    search_click("4_building_bell.png")

def Q_friend() :    #11친구애정주기
    search_click("4_building_bell.png")

def Q_reward() :    #12 업적 보상받기
    search_click("4_building_bell.png")


def logout() :
    mouse_move(800, 350, 840, 420)
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
    mouse_move(800, 350, 840, 420)
    # search_move("2_logout4.png")
    # time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    run()
    mouse_move(20, 200, 70, 310)
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    search_click("2_logout6.png")
    time.sleep(random.uniform(0.05001, 0.19987))



# def main():
#     #최종
#     search_click("0_tinyfarm.png")
#     search_click("0_tinyfarm.png")    #35초 ~38초..
#     id_str = 'agnus'
#     num = [0, 1, 2, 3, 4, 5, 7, 9]
#     pw = '1022'
#
#     for i in num :
#         id = id_str + num
#         print(datetime.today())
#         print(id)
#         login(id, pw)
#         # first()
#         # run_bell()
#         # run()
#         # logout()


def main(): #test용
    login('agnus0', '1022')
    # Q_hunt_1()
    # Q_animal()
    # Q_luckybag()
    # Q_safari()
    # Q_village()
    #
    # run()
    #
    # mouse_move(800, 350, 840, 420)
    # mouse_scroll(-1)
    # time.sleep(random.uniform(0.60001, 1.09999))
    #
    # run()
    #
    # Q_friend()
    # Q_hunt_2()


if __name__ == '__main__':
    main()


#3 완료
