# -*- coding:utf-8 -*-
from django.shortcuts import render


from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse


# Create your views here.
class DuplicateView(View):

    def get(self, request):
        return HttpResponse(u'重复数据，返回请重新录入!')
