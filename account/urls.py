#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-06-28 14:30 
@author: guolt
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    # url(r'^login/$', views.user_login, name='login'),

    url(r'^login/$','django.contrib.auth.views.login', name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login', name='logout_then_login'),
]




