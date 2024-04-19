from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^signup/$', views.signup),
    re_path(r'^login/$', views.login),
    re_path(r'^test_token/$', views.test_token),
    re_path(r'loginInfo', views.list_users),
]
