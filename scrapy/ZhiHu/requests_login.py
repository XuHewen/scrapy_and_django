import requests
import re
import http.cookiejar

import shutil

from scrapy import Selector

from zheye import zheye

session = requests.session()
session.cookies = http.cookiejar.LWPCookieJar(filename='cookes.txt')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookies 未能加载")

agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

headers = {
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
}


def is_login():
    inbox_url = 'https://www.zhihu.com/inbox'
    response = session.get(inbox_url, allow_redirects=False, headers=headers)
    if response.status_code == 302:
        return False
    else:
        return True


def get_xsrf():
    response = session.get("https://www.zhihu.com", headers=headers)
    # value = re.match(r'.*name="_xsrf"\svalue="(.*?)"', response.text)
    sel = Selector(response)
    xsrf_value = sel.xpath('/html/body/input/@value').extract()
    if len(xsrf_value) != 0:
        return xsrf_value[0]
    else:
        return ""


def get_index():
    response = session.get("https://www.zhihu.com", headers=headers)
    with open("index.html", "wb") as f:
        f.write(response.text.encode('utf-8'))
        print("OK")


def get_captcha():
    import time
    t = str(int(time.time() * 1000))
    url = 'https://www.zhihu.com/captcha.gif?r={}&type=login&lang=cn'.format(t)
    text = session.get(url, headers=headers, stream=True)

    if text.status_code == 200:
        with open('pic_capcha.gif', 'wb') as f:
            text.raw.decode_content = True
            shutil.copyfileobj(text.raw, f)

        z = zheye()
        return z.Recognize('pic_capcha.gif')
    else:
        return ''


def login(accout, passwd):
    if re.match(r'^1\d{10}', accout):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"

        pos = get_captcha()

        params = {
            '_xsrf': get_xsrf(),
            'password': passwd,
            'captcha': '{"img_size": [200, 44], "input_points": [[%.2f, %f], [%.2f, %f]]}' % (
                pos[0][1] / 2, pos[0][0] / 2, pos[1][1] / 2, pos[1][0] / 2),
            'captcha_type': 'cn',
            'phone_num': accout
        }

        r = session.post(post_url, params=params, headers=headers)
        session.cookies.save()
        print(r.text)
        print(r.status_code)


# login('18810266409', 'XXxx19911014')
# get_index()
is_login()
