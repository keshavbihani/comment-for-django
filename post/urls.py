from django.conf.urls import url
from django.contrib import admin

from .views import postList,postDetail


urlpatterns = [
	url(r'^$', postList, name='list'),
	url(r'^(?P<id>[\w-]+)/$', postDetail, name='detail'),	
]	