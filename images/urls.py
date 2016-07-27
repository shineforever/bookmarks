
#! /usr/bin/env python
# coding:utf-8
"""
Created on: 2016-07-27 15:47 
@author: guolt
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.image_create, name='create'),
]


