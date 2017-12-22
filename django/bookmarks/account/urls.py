from django.urls import path
from .views import UserLoginView, dashboard, LogoutView
from django.contrib.auth.views import login, logout, logout_then_login
from django.contrib.auth.views import password_change, password_change_done
from django.contrib.auth.views import (password_reset, password_reset_done,
                                       password_reset_confirm,
                                       password_reset_complete)
from bookmarks import settings


urlpatterns = [
    # path(r'login/', UserLoginView.as_view(), name='login'),
    path(r'login/', login, {'template_name': 'account/login.html'},
         name='login'),
    path(r'', dashboard, name='dashboard'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    # path(r'logout-then-login/',
    #      logout_then_login,
    #      name='logout_then_login'),

    path('password-change/', password_change, name='password_change'),
    path('password-change/done/', password_change_done,
         name='password_change_done'),
    
    path('password-reset/', password_reset, name='password_reset'),
    path('password-reset/done/', password_reset_done, name='password_reset_done'),
    path('password-reset/confirm/()', password_reset, name='password_reset'),
    path('password-reset/', password_reset, name='password_reset'),
]