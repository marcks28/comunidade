# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'$^', views.Index.as_view(), name='index')
]
