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

    #user profile
    url(r'^register/$',views.register, name='register'),

    #login and logout
    url(r'^login/$','django.contrib.auth.views.login', name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login', name='logout_then_login'),

    #change password
    url(r'^password-change/$','django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password-change/done/$','django.contrib.auth.views.password_change_done', name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$','django.contrib.auth.views.password_reset',name='password_reset'),
    url(r'^password-reset/done/$','django.contrib.auth.views.password_reset_done',name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$','django.contrib.auth.views.password_reset_confirm',
       name='password_reset_confirm'),
    url(r'^password-reset/complete/$','django.contrib.auth.views.password_reset_complete',
       name='password_reset_complete'),


]




