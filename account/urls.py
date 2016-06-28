#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-06-28 14:30 
@author: guolt
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
]




