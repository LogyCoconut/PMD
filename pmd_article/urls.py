from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.index),
    re_path('^p/(\d+)$', views.detail),
    re_path('^w/(\d+)$', views.write),
    re_path('^save(\d+)$', views.save)
]