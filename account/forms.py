#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-06-28 14:06 
@author: guolt
"""

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
