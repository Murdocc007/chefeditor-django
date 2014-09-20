from django.conf.urls import patterns, url

from chefeditor import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='home'),
        url(r'^home/$', views.index),
        url(r'^home/(?P<loginFail>\d+)/', views.index),
        url(r'^explore/$', views.explore),
        url(r'^explore/(?P<genre_id>\d+)/', views.explore),
        url(r'^profile/', views.view_profile),
        url(r'^user/edit/', views.user_edit, name='user_edit'),
        url(r'^viewtemplate/(?P<login_id>\d+)/(?P<template_name>\w+)/', views.view_template),
        url(r'^checklogin/', views.checkLogin),
        url(r'^logout/', views.logout),
        url(r'^save/', views.save_template),
        url(r'^modify/', views.modify_template),
        url(r'^fblogin/', views.fblogin),
        url(r'^checkFBLogin/', views.checkFBLogin),



)
