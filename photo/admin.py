#coding:utf-8
from django.contrib import admin
from photo.models import *
admin.autodiscover()
admin.site.register(Item,ItemAdmin)
admin.site.register(Photo)