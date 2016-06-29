#! /usr/bin/env python
# coding:utf-8

"""
Created on: 2016-06-28 14:06
@author: guolt
"""
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    """
    用户认证
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm
    return render(request,'account/login.html',{'form':form})


@login_required
def dashboard(request):
    # return HttpResponse("OK")

    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


