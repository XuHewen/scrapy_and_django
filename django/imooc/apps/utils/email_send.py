from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from imooc.settings import EMAIL_FROM


def random_str(str_length=8):
    str_r = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(str_length):
        str_r += chars[random.randint(0, length)]
    return str_r


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '注册'
        email_body = '点击链接激活: http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body,
                                EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = '密码重置'
        email_body = '点击链接激活: http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body,
                                EMAIL_FROM, [email])
        if send_status:
            pass
