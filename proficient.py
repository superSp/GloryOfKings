import os
from time import sleep
import cv2
import time
import aircv as ac
import random

repeat_times = 10

hero_pos = ('./hero/miyue.png', './hero/baiqi.png', './hero/zhaoyun.png',
            './hero/mozi.png')


def check_img(target, sleep_seconds):
    while True:
        match_value = match(cv2.imread(target), get_screen())
        print('循环检测' + target + '中' + '匹配度=' + match_value.__str__())
        if 0.7 <= match_value:
            return
        else:
            sleep(sleep_seconds)


def choose_hero():
    imsrc = get_screen()
    hero_name = hero_pos[random.randint(0, hero_pos.__len__() - 1)]
    imobj = ac.imread(hero_name)
    print('这把玩' + hero_name)
    # find the match position
    pos = ac.find_template(imsrc, imobj, threshold=0.3)

    circle_center_pos = pos['result']
    touch(circle_center_pos[0], circle_center_pos[1], 4)


def begin_match():
    print('点击匹配')
    touch(700, 600)

    check_img('./imgs/match.jpg', 1)

    print('检测到已经匹配成功，点击接受')
    touch(645, 602, 4)

    print('点击扩大，显示所有英雄')
    touch(258, 362, 4)

    print('选择要玩的英雄')
    choose_hero()

    print('点击确认，等待10分钟' + print_time())
    touch(1200, 680, 5)
    touch(1200, 680, 60 * 10)

    check_img('./imgs/game_end.png', 60)


def end_match():
    print('结束节点1，点击继续')
    touch(530, 620, 7)

    print('结束节点2，点击继续')
    touch(650, 650, 4)

    print('结束节点3，点击继续')
    touch(650, 650, 4)

    print('结束节点4，点击继续')
    touch(740, 650, 4)


def do_first_work():
    print('点击竞技对抗')
    touch(555, 555)
    print('点击王者峡谷')
    touch(222, 222)
    print('点击人机')
    touch(600, 400, 2)
    print('点击开始练习')
    touch(1100, 530, 8)


def do_second_work():
    begin_match()

    end_match()


def print_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


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
    return maxres


def touch(x, y, second=1):
    os.system('adb -s emulator-5554  shell input tap {} {}'.format(x, y))
    sleep(second)


if __name__ == '__main__':
    do_first_work()
    for i in range(repeat_times):
        print('第' + i.__str__() + '次任务')
        do_second_work()
