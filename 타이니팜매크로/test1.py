import pyautogui as pag
import random, time, subprocess
import mss, cv2
import numpy as np
from datetime import datetime

from imagesearch import *  #https://github.com/drov0/python-imagesearch


def sleep_0():
    time.sleep(random.uniform(0.05001, 0.19987))


def sleep_1() :
    time.sleep(random.uniform(0.45001, 1.29987))


def sleep_2() :
    time.sleep(random.uniform(1.05001, 1.79987))



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
        sleep_0()
        img = cv2.imread(img)
        height, width, channels = img.shape
        offset = min(height, width)
        pyautogui.moveTo(pos[0] + r(width, -offset), pos[1] + r(height, -offset),
                         duration)
        sleep_1()
        pyautogui.click(button=action)


# x: 100              y : 70
# x: 750              y : 420
def search_click_range(img, action='left'):
    duration=random.uniform(0.3, 0.7)
    pos = imagesearch(img)
    # print(pos[0], pos[1])
    if pos[0] != -1:
        if pos[0]>= 100 and pos[0] < 750 and pos[1] >= 70 and pos[1] < 420 :
            sleep_0()
            img = cv2.imread(img)
            height, width, channels = img.shape
            offset = min(height, width)
            pyautogui.moveTo(pos[0] + r(width, -offset), pos[1] + r(height, -offset),
                             duration)
            sleep_1()
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
    sleep_0()
    search_click('1_login4.png')                       #logout
    time.sleep(random.uniform(2.5001, 3.9987))

    #id 입력
    search_click('1_login1.png')
    sleep_2()
    pyautogui.press('end')
    sleep_1()
    #backspace 7번
    pyautogui.press('backspace')
    sleep_0()
    pyautogui.press('backspace')
    sleep_0()
    pyautogui.press('backspace')
    sleep_0()
    pyautogui.press('backspace')
    sleep_0()
    pyautogui.press('backspace')
    sleep_0()
    pyautogui.press('backspace')
    sleep_0()
    pyautogui.press('backspace')
    sleep_0()
    # pyautogui.press('backspace')
    pyautogui.typewrite(id, random.uniform(0.30001, 0.69999)) #한글 입력은 안 됨
    sleep_1()
    pyautogui.press('tab')                           #pw 입력
    sleep_1()
    pyautogui.typewrite(pw, random.uniform(0.30001, 0.69999))
    # pyautogui.press('tab')
    # pyautogui.press('Enter')
    sleep_2()
    sleep_0()
    search_click('1_login2.png')
    time.sleep(random.uniform(2.5001, 4.9987))
    pos = imagesearch("1_login3.png")
    if pos[0] != -1:
        search_click("1_login3.png")
        time.sleep(random.uniform(1.55001, 2.79987))
    else :
        print("somethine wrong~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



def first() :   #로그인시 클릭해야할것들 1
    pos = imagesearch("1_login4.png")
    while pos[0] != -1:
        pos = imagesearch("1_login4.png")
        sleep_2()

    print("loopout")
    presence = imagesearch("3_first1.png")
    if (presence[0] != -1) :
        search_click("3_first1.png")
        sleep_2()
        search_click("3_first2.png")
        sleep_2()
        search_click("3_first3.png")
        sleep_2()
        search_click("3_first4.png")
        sleep_2()

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
        # Q_reward()



def run_bell() :  #벨트리, 러브하우스 클릭
    max_retries = 2
    retries  = 0
    while True:
        if retries >= max_retries:
            sleep_2()
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
            sleep_2()
            break
        presence = imagesearch("5_food1.png")
        if (presence[0] == -1):
            retries += 1
            continue
        else :
            search_click_range("4_building2.png")

            search_click_range("5_food1.png")
            search_click_range("5_food2.png")

            search_click_range("friend1.png")
            search_click_range("friend2.png")
            search_click_range("friend3.png")

            search_click_range("2_logout4_building1.png")
            continue



def Q_hunt_1() :    #6모험가 확인
    sleep_1()
    search_click_range("Q_hunt_1_1.png")
    sleep_2()
    search_click_range("Q_hunt_1_2.png")
    sleep_1()

    max_retries = 3
    retries  = 0
    while True:
        if retries >= max_retries:
            search_click("Q_hunt_1_5.png")
            sleep_2()
            break
        # presence = imagesearch("5_food1.png")
        # if (presence[0] != -1):
        search_click_range("Q_hunt_1_3.png")
        search_click_range("Q_hunt_1_3_1.png")
        sleep_2()
        search_click_range("Q_hunt_1_4.png")
            # continue
        # else :
        retries += 1
        continue



def Q_hunt_2() :    #6모험가 모험 보내기
    search_click("Q_hunt_1_1.png")
    sleep_0()
    search_click("Q_hunt_1_1.png")
    sleep_2()
    max_retries = 1
    retries  = 0
    pos = imagesearch("Q_hunt_2_2.png")
    while pos[0] == -1 :
        if retries >= max_retries:
            search_click("Q_hunt_1_5.png")
            search_click("Q_hunt_1_5.png")
            sleep_2()
            break

        #모험가 첫번째 칸
        mouse_scroll(-1)
        sleep_1()
        mouse_move(400, 300, 450, 350)
        sleep_0()
        pyautogui.click(button='left')
        sleep_1()

        mouse_scroll(-1)
        sleep_1()
        mouse_move(510, 220, 610, 320)
        sleep_0()
        pyautogui.click(button='left')
        sleep_1()

        #모험가 확인
        # mouse_scroll(-1)
        sleep_1()
        pos = imagesearch("Q_hunt_2_2.png")
        if pos[0] != -1:
            search_click("Q_hunt_2_2.png")
            sleep_1()
            pos = imagesearch("Q_hunt_2_2_1.png")
            if pos[0] != -1:
                search_click("Q_hunt_2_2_1.png")
                search_click("Q_hunt_1_5.png")
                sleep_2()
                break
            search_click("Q_hunt_2_3.png")
            pos = imagesearch("Q_hunt_1_1.png")
            continue

        #모험가 두번째 칸
        mouse_move(480, 300, 530, 350)
        sleep_0()
        pyautogui.click(button='left')
        sleep_1()

        mouse_scroll(-1)
        sleep_1()
        mouse_move(510, 220, 610, 320)
        sleep_0()
        pyautogui.click(button='left')
        sleep_1()

        #모험가 확인
        # mouse_scroll(-1)
        sleep_1()
        pos = imagesearch("Q_hunt_2_2.png")
        if pos[0] != -1:
            search_click("Q_hunt_2_2.png")
            sleep_1()
            pos = imagesearch("Q_hunt_2_2_1.png")
            if pos[0] != -1:
                search_click("Q_hunt_2_2_1.png")
                search_click("Q_hunt_1_5.png")
                sleep_2()
                break
            search_click("Q_hunt_2_3.png")
            pos = imagesearch("Q_hunt_1_1.png")
            continue

        #모험가 세번째 칸
        mouse_move(560, 300, 610, 350)
        sleep_0()
        pyautogui.click(button='left')

        sleep_1()
        mouse_scroll(-1)
        sleep_1()
        mouse_move(510, 220, 610, 320)
        sleep_0()
        pyautogui.click(button='left')
        sleep_1()

        #모험가 확인
        # mouse_scroll(-1)
        sleep_1()
        pos = imagesearch("Q_hunt_2_2.png")
        if pos[0] != -1:
            search_click("Q_hunt_2_2.png")
            sleep_1()
            pos = imagesearch("Q_hunt_2_2_1.png")
            if pos[0] != -1:
                search_click("Q_hunt_2_2_1.png")
                search_click("Q_hunt_1_5.png")
                sleep_2()
                break
            search_click("Q_hunt_2_3.png")
            pos = imagesearch("Q_hunt_1_1.png")
            continue

        retries += 1
        continue



def Q_animal() :    #7교배소
    search_click("Q_animal_1.png")
    sleep_1()
    search_click("Q_animal_1_1.png")
    sleep_1()
    mouse_move(450, 320, 720, 350)
    sleep_0()
    pyautogui.click(button='left')
    sleep_1()

    search_click("Q_animal_2.png")
    sleep_1()
    search_click("Q_animal_3.png")
    sleep_2()
    sleep_2()
    sleep_2()
    search_click("Q_animal_4.png")
    sleep_1()
    search_click("Q_animal_5.png")

    pos = imagesearch("Q_animal_6.png")
    max_retries = 3
    retries  = 0
    while pos[0] == -1:
        if retries >= max_retries:
            break
        pos = imagesearch("Q_animal_6.png")
        sleep_1()
        retries += 1
        continue

    sleep_2()
    print("교배소 확인누르기")
    search_click("Q_animal_6.png")
    sleep_2()
    sleep_2()
    sleep_2()
    print("엑스 안누르나??")
    search_click("Q_animal_7.png")
    sleep_1()



def Q_luckybag() :  #8럭키백
    mouse_move(800, 70, 840, 100)
    sleep_0()
    pyautogui.click(button='left')
    sleep_1()
    search_click("Q_luckbag1.png")
    sleep_1()
    search_click("Q_luckbag2.png")
    sleep_1()
    search_click("Q_luckbag3.png")
    sleep_1()
    search_click("Q_luckbag3.png")
    sleep_2()
    sleep_2()
    sleep_2()
    sleep_2()
    sleep_2()
    sleep_2()
    search_click("Q_luckbag4.png")
    sleep_1()
    search_click("Q_luckbag5.png")
    sleep_1()
    sleep_2()
    sleep_2()
    print("럭키백 끝")



def Q_safari() :    #9사파리
    mouse_move(800, 200, 840, 240)
    sleep_0()
    pyautogui.click(button='left')
    sleep_1()
    search_click("Q_safari1.png")
    sleep_1()
    search_click("Q_safari2.png")

    pos = imagesearch("Q_safari3_1.png")
    while pos[0] == -1:
        pos = imagesearch("Q_safari3_1.png")
        sleep_1()

    sleep_2()
    print("사파리 나가기")
    search_click("Q_safari3.png")
    sleep_1()
    search_click("Q_safari4.png")
    sleep_2()
    search_click("Q_safari5.png")
    sleep_1()
    sleep_2()
    sleep_2()



def Q_village() :    #10마을 출석, 애정환원
    mouse_move(20, 270, 70, 310)
    sleep_0()
    pyautogui.click(button='left')
    sleep_2()
    search_click("Q_village1.png")
    sleep_1()
    search_click("Q_village2.png")
    sleep_1()
    search_click("Q_village2_1.png")
    sleep_2()
    search_click("Q_village3.png")
    sleep_1()
    pos = imagesearch("Q_village3_1.png")
    while pos[0] != -1:
        search_click("Q_village3_1.png")
        sleep_1()
        mouse_move(240, 425, 300, 440)
        sleep_0()
        pyautogui.click(button='left')
        sleep_2()
        search_click("Q_village3_2.png")
        sleep_1()
        search_click("Q_village3_3.png")
        sleep_1()
        pos = imagesearch("Q_safari3_1.png")
        sleep_1()
    # pos = imagesearch("Q_hunt_2_2.png")
    # while pos[0] == -1 :
    search_click("Q_village4.png")
    sleep_1()



def Q_friend() :    #11친구애정주기
    mouse_move(30, 480, 70, 500)
    sleep_0()
    pyautogui.click(button='left')
    sleep_0()
    pyautogui.click(button='left')
    sleep_2()
    #알프레도 농장
    mouse_move(450, 170, 720, 250)
    sleep_0()
    pyautogui.click(button='left')
    sleep_0()
    pyautogui.click(button='left')

    sleep_2()
    sleep_2()
    sleep_2()
    sleep_2()

    search_click("Q_friend1.png")
    sleep_2()
    search_click("Q_friend1.png")
    sleep_2()
    search_click("Q_friend1.png")
    sleep_1()
    # mouse_move(370,385, 500, 410)
    pyautogui.click(button='left')
    sleep_2()

    search_click("Q_friend2.png")
    sleep_1()
    search_click("Q_friend2_1.png")
    sleep_1()


    for i in range(0, 16) :
        mouse_move(815, 330, 830, 370)
        mouse_move(815, 330, 830, 370)
        sleep_0()
        pyautogui.click(button='left')
        sleep_0()

        sleep_2()
        sleep_2()

        search_click("Q_friend1.png")
        sleep_2()
        search_click("Q_friend1.png")
        sleep_1()
        search_click("Q_friend1.png")
        sleep_0()
        # mouse_move(370,385, 500, 410)
        # pyautogui.click(button='left')
        # sleep_2()

        search_click("Q_friend2.png")
        sleep_1()
        search_click("Q_friend2_1.png")
        sleep_1()

    print("go myfarm")
    search_click("Q_friend3.png")
    sleep_0()
    search_click("Q_friend3.png")

    pos = imagesearch("Q_friend4.png")
    while pos[0] != -1:
        pos = imagesearch("Q_friend4.png")
        sleep_1()


##############################################
def Q_farm() :      #12 밭 수거
    search_click("4_building_bell.png")



def Q_reward() :    #13 업적 보상받기
    mouse_move(20, 200, 70, 240)
    sleep_0()
    pyautogui.click(button='left')
    sleep_2()
    sleep_2()

    pos = imagesearch("Q_reward1.png")
    while pos[0] != -1:
        pos = imagesearch("Q_reward1.png")
        search_click("Q_reward1.png")
        sleep_2()
        search_click("Q_reward2.png")
        sleep_2()

    search_click("Q_reward3.png")
    sleep_1()

    pos = imagesearch("Q_reward1.png")
    while pos[0] != -1:
        pos = imagesearch("Q_reward1.png")
        search_click("Q_reward1.png")
        sleep_2()
        search_click("Q_reward2.png")
        sleep_2()

    search_click("Q_reward4.png")
    sleep_1()



def logout() :
    mouse_move(800, 350, 840, 420)
    # search_move("2_logout1.png")
    # time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    sleep_1()
    mouse_scroll(-1)
    sleep_1()

    run()

    search_click("2_logout2.png")
    sleep_1()

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
    sleep_0()
    run()

    pos = imagesearch("2_logout6.png")
    while pos[0] == -1:
        mouse_move(20, 200, 70, 310)
        sleep_1()
        mouse_scroll(-1)
        sleep_1()
        pos = imagesearch("2_logout6.png")

    search_click("2_logout6.png")
    sleep_0()



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

#Q_farm()
#         # run_bell()
#         # run()
#         # logout()


def main(): #test용
    login('agnus0', '1022')
    first()
    run_bell()
    Q_hunt_1()
    Q_animal()
    Q_luckybag()
    Q_safari()
    Q_village()

    run()

    mouse_move(800, 350, 840, 420)
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    #
    run() #+확인버튼
    #프렌드 막히는 부분 수정하기
    Q_friend()
    #나갔다 오는게 나을듯..
    Q_hunt_2()
    Q_reward()

    logout()

if __name__ == '__main__':
    main()


#3 완료
