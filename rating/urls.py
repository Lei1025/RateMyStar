from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static

from rating import views

from django.contrib.staticfiles import views as views2

urlpatterns = [
    url(r'^upload', views.upload),
    url(r'^show', views.showImg),
    url(r'^register',views.register),
    url(r'^login',views.user_login),
    url(r'^index',views.index),
    url(r'^$',views.index),
    url(r'^forgotpassword',views.forgot_password),
    url(r'^123', views.index_content),
    url(r'^detail-(?P<name>.*$)',views.detail),
    url(r'^category-(?P<name>.*$)',views.category),
    url(r'^logout',views.user_logout,name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)