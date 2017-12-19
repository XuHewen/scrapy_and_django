import shutil
import requests
import re
from http import cookiejar
from scrapy import Selector

from zheye import zheye


class ZhiHu(object):

    def __init__(self, accout, passwd):
        self.accout = accout
        self.passwd = passwd

        self.session = requests.Session()
        self.session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')

        try:
            self.session.cookies.load(ignore_discard=True)
        except:
            print("cookies 未能加载")

        self.headers = {
            'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
        }

        self.login()
        self.get_index()

    def is_login(self):
        inbox_url = 'https://www.zhihu.com/inbox'
        response = self.session.get(inbox_url,
                                    allow_redirects=False,
                                    headers=self.headers)
        if response.status_code == 302:
            return False
        else:
            return True

    def get_xsrf(self):
        response = self.session.get("https://www.zhihu.com",
                                    headers=self.headers)
        sel = Selector(response)
        xsrf_value = sel.xpath('/html/body/input/@value').extract()
        if len(xsrf_value) != 0:
            return xsrf_value[0]
        else:
            return ""

    def get_index(self):
        response = self.session.get("https://www.zhihu.com",
                                    headers=self.headers)
        with open("index.html", "wb") as f:
            f.write(response.text.encode('utf-8'))
            print("OK")

    def get_captcha(self):
        import time
        t = str(int(time.time() * 1000))
        url = 'https://www.zhihu.com/captcha.gif?r={}&type=login&lang=cn'.format(t)
        response = self.session.get(url, headers=self.headers, stream=True)

        if response.status_code == 200:
            with open('pic_capcha.gif', 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)

            z = zheye()
            return z.Recognize('pic_capcha.gif')
        else:
            return ''

    def login(self):
        if self.is_login():
            print("已经登录")
            return

        if re.match(r'^1\d{10}', self.accout):
            print("手机号码登录")
            post_url = "https://www.zhihu.com/login/phone_num"

            pos = self.get_captcha()

            params = {
                '_xsrf': self.get_xsrf(),
                'password': self.passwd,
                'captcha': '{"img_size": [200, 44], "input_points": [[%.2f, %f], [%.2f, %f]]}' % (
                    pos[0][1] / 2, pos[0][0] / 2, pos[1][1] / 2, pos[1][0] / 2),
                'captcha_type': 'cn',
                'phone_num': self.accout
            }

            self.session.post(post_url, params=params, headers=self.headers)
            self.session.cookies.save()


zhihu = ZhiHu('18810266409', 'XXxx19911014')
