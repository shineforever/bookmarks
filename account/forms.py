#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-06-28 14:06 
@author: guolt
"""

# from django import forms
# from django.conf import settings
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Profile

from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    """
    用户注册模块
    """
    password = forms.CharField(label='Input your password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        """
        判断两次输入的密码是否一致
        :return:
        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password don't match")
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')





