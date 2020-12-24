import os
import cv2
from time import sleep
import aircv as ac
import random

hero_pos = ('./hero/houyi.png', '2', '3', '4', 5)


def get_screen():
    # 截屏口令
    cmd_get = 'adb shell screencap -p /sdcard/screen_img.png'
    # 发送图片口令
    cmd_send = 'adb pull sdcard/screen_img.png ./screen.png'
    # 截屏和发送操作
    os.system(cmd_get)
    os.system(cmd_send)
    img = cv2.imread('./screen.png')
    return img


def match(img1, template):
    """img1代表待匹配图像, template代表模板, 模板是小图"""
    res = cv2.matchTemplate(img1, template, cv2.TM_CCOEFF_NORMED)
    maxres = res.max()
    # 将匹配度返回
    return maxres


def check_img(target, sleep_seconds):
    while True:
        print('循环检测' + target + '中')
        if 0.9 <= match(cv2.imread(target), get_screen()):
            return
        else:
            sleep(sleep_seconds)


if __name__ == '__main__':
    # get_screen()
    # 读取目标图片
    # target = cv2.imread("./imgs/match.jpg")
    # # # 读取模板图片
    # template = cv2.imread('screen.png')
    # print(match(target, template))
    # check_img('./imgs/match.jpg', 1)

    # imsrc = ac.imread('./imgs/game_end.png')
    # imobj = ac.imread('./imgs/game_endtmp.jpg')
    # print(match(imsrc, imobj))
    # # find the match position
    # pos = ac.find_template(imsrc, imobj)
    #
    # circle_center_pos = pos['result']
    # print(pos.__str__())
    print(hero_pos[random.randint(0, hero_pos.__len__() - 1)])
