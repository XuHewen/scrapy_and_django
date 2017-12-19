# -*- coding:utf-8 -*-
from django import forms
from .models import LeaderProfile


class LeaderProfileForm(forms.ModelForm):
    birth_of_year = forms.CharField(label=u'出生年', required=False, min_length=4,
                                    max_length=4, help_text=u'4位数字')
    birth_of_month = forms.CharField(label=u'出生月', required=False, min_length=4,
                                     max_length=2, help_text=u'2位数字')
    birth_of_day = forms.CharField(label=u'出生日', required=False, min_length=4,
                                   max_length=2, help_text=u'2位数字')
    
    # def save(self, commit=True):
    #     extra_field = self.cleaned_data.get('extra_field', None)
    #     # ...do something with extra_field here...
    #     return super(LeaderProfileForm, self).save(commit=commit)

    class Meta:
        model = LeaderProfile
        fields = '__all__'
        # fields = ['birth_of_year']
