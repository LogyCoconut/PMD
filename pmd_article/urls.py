from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.index),
    re_path('^p/(\d+)$', views.detail),
    re_path('^w/(\d+)$', views.write),
    re_path('^save(\d+)$', views.save),
    re_path('^del(\d+)$', views.delete),
    re_path('^login$', views.login),
    re_path('^login_deal$', views.login_deal),
]