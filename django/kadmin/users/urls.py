from django.urls import path
from .views import UserLoginView, UserProfileView, UserLogoutView


urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('profile', UserProfileView.as_view(), name='profile'),
    path('logout', UserLogoutView.as_view(), name='logout')
]