from django import forms
from captcha.fields import CaptchaField


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    # captcha = CaptchaField(error_messages={'invalid': '验证码错误'})