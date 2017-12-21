# -*- coding:utf-8 -*-
from django import forms
from .models import PunishmentModel


class PunishmentForm(forms.ModelForm):
    
    punished_reason = forms.CharField(widget=forms.Textarea,
                                      required=False,
                                      label=u'处罚原因')
    content = forms.CharField(widget=forms.Textarea, required=False,
                              label=u'原文')

    class Meta:
        model = PunishmentModel
        fields = '__all__'
        # fields = ['birth_of_year']
