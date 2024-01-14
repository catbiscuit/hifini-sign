import json
import os
import time

import requests
import random


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


def sign(cookie, bark_deviceKey, bark_icon, no):
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

        title = 'HiFiNi-签到结果 - 第' + str(no) + '个'
        message = ''

        if "成功签到" in response.text:
            message = '成功签到'
        elif "今天已经签过啦" in response.text:
            message = '今天已经签过啦'
        elif "维护中" in response.text:
            message = '服务器正在维护'
        else:
            message = '签到结果解析错误'

        bark(bark_deviceKey, title, message, bark_icon)

    else:
        print('不执行签到')


def main():
    bark_device_key = os.environ.get('BARK_DEVICEKEY')
    bark_icon = os.environ.get('BARK_ICON')

    wait = random.randint(3, 110)
    time.sleep(wait)

    for i in range(1, 4):
        cookie = os.environ.get('COOKIE' + str(i))
        sign(cookie, bark_device_key, bark_icon, i)

        sm = random.randint(19, 97)
        time.sleep(sm)

    print('finish')


if __name__ == '__main__':
    main()
