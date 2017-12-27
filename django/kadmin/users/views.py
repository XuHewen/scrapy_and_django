from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .forms import UserLoginForm


# Create your views here.
class UserLoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            user_login_form = UserLoginForm()

            return render(request, 'Login.html',
                          {'user_login_form': user_login_form})

    def post(self, request):
        user_login_form = UserLoginForm(request.POST)

        if user_login_form.is_valid():

            cd = user_login_form.cleaned_data

            user = authenticate(username=cd['username'],
                                password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return render(request, 'index.html')
                    return redirect('index')
            else:
                return render(request, 'Login.html',
                              {'user_login_form': user_login_form,
                               'msg': '用户名或密码错误'})
        else:
            return render(request, 'Login.html',
                          {'user_login_form': user_login_form})


@login_required
def index(request):
    return render(request,
                  'index.html')


class UserProfileView(View):

    def get(self, request):
        return render(request, 'profile.html')


class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')