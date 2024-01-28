import json
import os
import random
import re
import time

import requests


def bark(device_key, title, content, bark_icon):
    if not device_key:
        return 2

    url = "https://api.day.app/push"
    headers = {
        "content-type": "application/json",
        "charset": "utf-8"
    }
    data = {
        "title": title,
        "body": content,
        "device_key": device_key
    }

    if not bark_icon:
        bark_icon = ''
    if len(bark_icon) > 0:
        url += '?icon=' + bark_icon
        print('拼接icon')
    else:
        print('不拼接icon')

    resp = requests.post(url, headers=headers, data=json.dumps(data))
    resp_json = resp.json()
    if resp_json["code"] == 200:
        print(f"[Bark]Send message to Bark successfully.")
    if resp_json["code"] != 200:
        print(f"[Bark][Send Message Response]{resp.text}")
        return -1
    return 0


def sign(cookie, no):
    pre = '第' + str(no) + '个，'
    if not cookie:
        cookie = ''

    if len(cookie) > 0:
        print('有cookie，需要执行签到')

        url = 'https://www.hifini.com/sg_sign.htm'
        headers = {
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.post(url, headers=headers)

        print(response.text)

        message = ''

        if "成功签到" in response.text:
            message = '成功签到'
        elif "今天已经签过啦" in response.text:
            message = '今天已经签过啦'
        elif "维护中" in response.text:
            message = '服务器正在维护'
        else:
            message = '签到结果解析错误'

        return pre + message

    else:
        print('不执行签到')
        return ''


def main():
    bark_device_key = os.environ.get('BARK_DEVICEKEY')
    bark_icon = os.environ.get('BARK_ICON')

    wait = random.randint(3, 110)
    time.sleep(wait)

    message_all = []
    title = 'HiFiNi-签到结果'
    message = ''
    for i in range(1, 4):
        cookie = os.environ.get('COOKIE' + str(i))
        msg = sign(cookie, i)
        if not msg:
            msg = ''
        if len(msg) > 0:
            message_all.append(msg)

        sm = random.randint(19, 97)
        time.sleep(sm)

    if not message_all:
        message = '暂无执行结果'
    else:
        message_all = '\n'.join(message_all)
        message_all = re.sub('\n+', '\n', message_all).rstrip('\n')
        message = message_all

    bark(bark_device_key, title, message, bark_icon)

    print('finish')


if __name__ == '__main__':
    main()
