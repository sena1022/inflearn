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


# pag.mouseDown()
# time.sleep(random.uniform(0.15001, 0.29987))
# pag.mouseUp()
# time.sleep(random.uniform(0.05001, 0.25987))


#마우스 드래그
def mouse_drag(from_x, from_y, to_x, to_y) :
    drag = {
        'from': {
            'x': from_x,
            'y': from_y
        },
        'to': {
            'x': to_x,
            'y': to_y
        }
    }
    drag_start_x = random.uniform(drug['from']['x'], drug['from']['x']+100)
    drag_end_x = random.uniform(drug['from']['x']+100, drug['to']['x'])
    #
    drag_start_y = random.uniform(drug['from']['y'], drug['from']['y']+100)
    drag_end_y = random.uniform(drug['from']['y']+100, drug['to']['y'])
    #
    pag.moveTo(drag_start_x, drag_start_y, duration=random.uniform(0.30001, 0.69999))
    pag.dragTo(drag_end_x, drag_end_y, random.uniform(0.30001, 0.69999), button='left')




#http://blog.gilbok.com/python-glance-at-pyautogui-mobule/
#마우스 스크롤
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





    search_click("4_building2.png")
    search_click("5_food1.png")


def logout() :
    search_move("2_logout1.png")
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    search_click("2_logout2.png")
    time.sleep(random.uniform(1.05001, 1.79987))
    search_click("2_logout3.png")
    time.sleep(random.uniform(1.55001, 2.79987))

    #터틀맵 입장
    while True:
        presence = imagesearch("5_food1.png")
        if (presence[0] == -1):
            break
        else :
            search_click("4_building2.png")
            search_click("5_food1.png")
            continue

    search_move("2_logout4.png")
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)

    while True:
        presence = imagesearch("5_food1.png")
        if (presence[0] == -1):
            break
        else :
            search_click("4_building2.png")
            search_click("5_food1.png")
            continue

    time.sleep(random.uniform(0.80001, 1.89999))
    search_move("2_logout5.png")
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    mouse_scroll(-1)
    time.sleep(random.uniform(0.60001, 1.09999))
    search_click("2_logout6.png")
    time.sleep(random.uniform(0.05001, 0.19987))



def first() :
    search_click("3_first1.png")
    time.sleep(random.uniform(1.05001, 1.79987))
    search_click("3_first2.png")
    time.sleep(random.uniform(1.05001, 1.79987))
    search_click("3_first3.png")
    time.sleep(random.uniform(1.05001, 1.79987))
    search_click("3_first4.png")
    time.sleep(random.uniform(1.05001, 1.79987))
    search_click("4_building1.png")
    time.sleep(random.uniform(1.05001, 1.79987))
    search_click("4_building1.png")
    time.sleep(random.uniform(1.05001, 1.79987))
    run()



# def click_food() :





# def click_building() :






def main():
    search_click("0_tinyfarm.png")
    search_click("0_tinyfarm.png")    #35초 ~38초..


    id_str = 'agnus'
    num = [0, 1, 2, 3, 4, 5, 7, 9]

    for i in num :
        id = id_str + num
        print(datetime.today())
        print(id)
        login()
        time.sleep(random.uniform(1.55001, 2.79987))

        presence = imagesearch("3_first1.png")
        if (presence[0] == -1) :
            run()

        else :
            first()

    #모헙가

    #교배소

    #출석

    #수확
    #벨, 애정, 경험치, 골드
    #친구애정
    #먹이


    #럭키백
    #사파리

    #친구 애정
    #모험가

    #터틀맵

    #종료


    logout()



if __name__ == '__main__':
    main()




# 조합 키 입력하기 (쉬프트 누르고 왼쪽으로 한 칸 선택한 후, 쉬프트 떼기)
# pyautogui.keyDown('shift')
# pyautogui.press('left')
# pyautogui.keyUp('shift')

# Ctrl + C
# pyautogui.hotkey('ctrl', 'c')
# Ctrl + V
# pyautogui.hotkey('ctrl', 'v')




#마우스 위치 받기
# while True:
#     x, y = pag.position()
#     # position_str = 'X: ' + str(x) + 'Y: ' + str(y)
#     print('x: %s, y: %s' % (x,y))

## 윈도우 창 맨 위로
# def bring_window() :
#     time.sleep(0.5)
#     apple = """
#     tell application "BlueStacks"
#         activate
#     end tell
#     """
#     apple = apple.encode()
#     p = subprocess.Popen('osascript', stdin=subprocess.PIPE, stdout=subprocess.PIPE,
#     stderr=subprocess.STDOUT)
#     p.communicate(apple)[0]


#icon position
#button position
#mss 이미지 잡기
# with mss.mss() as sct:
#     A_img = np.array(sct.grab(A_icon))[:,:,3]
#     B_img = np.array(sct.grab(B_icon))[:,:,3]

# def compute_icon_type(img):
#     mean = np.mean(img, axix=(0,1))
#
#     if mean[0] > 50 and mean[0] < 55 and mean[1] >50 and mean[1] <55
#         and mean[2] > 50 and mean[2] <55:
#         results = 'icon_A'



#화면에 초 나오게..
# def countdown(t):
#     while t:
#         # mins, secs = divmod(t, 60)
#         # timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         timeformat = '{:02d}'.format(secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         t -= 1



#이미지 서치&클릭 - 파일명 영문으로만
# def search_img(img) :
#     pos = imagesearch(img)
#     if pos[0] != -1:
#         time.sleep(r(0.1, 0.2))
#         click_image(img, pos, 'left', 0.1)


# pos = imagesearcharea("1_login3.png", 0, 0, 860, 600)
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0], pos[1])
#     time.sleep(r(0.4, 0.2))
#     pyautogui.click(button="right")
# else:
#     print("image not found")
#
#
#
#
#
#     # pyautogui.click(button="right")
#     time.sleep(r(0.4, 0.2)) # the r function simply returns 0.4 + 0.2 * random.random()
#     presence = imagesearch("harvest_icon.png")
#
#     if (presence[0] == -1):
#       # do things
#
#
# pos = imagesearch_region_loop("github.png",0.5, 0,0,800,600)
# print("image found ", pos[0], pos[1])
#
#
# # click image is to be used after having found the image
#
# pos = imagesearch("github.png")
# if pos[0] != -1:
#     click_image("github.png", pos, "right", 0.2, offset=5)
