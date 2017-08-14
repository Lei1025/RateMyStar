from django.conf import settings
from django.conf.urls import url

from rating import views

urlpatterns = [
    url(r'^upload', views.uploadImg),
    url(r'^show', views.showImg),
    url(r'^register',views.register),
    url(r'^login',views.user_login),
    url(r'^index',views.index),
    url(r'^$',views.index),
    url(r'^forgotpassword',views.forgot_password),
    url(r'^123', views.index_content),
    url(r'^detial',views.detail)

]