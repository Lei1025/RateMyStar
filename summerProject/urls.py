"""summerProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from rating import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings
from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('rating.urls', namespace='rating')),
]

#urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += [
        url(r'(?P<path>.*/css.*)$', views.serve),
        url(r'(?P<path>.*/images.*)$', views.serve),
        url(r'(?P<path>.*/js.*)$', views.serve),
        url(r'(?P<path>.*/a_data.*)$', views.serve),
        url(r'(?P<path>.*/font.*)$', views.serve),
        url(r'(?P<path>.*/review.*)$', views.serve),

       # url(r'^css/(?P<path>.*)$', views.serve,{ 'document_root': '/static/css'}),
        #url(r'^js/(?P<path>.*)$', views.serve),
        #url(r'^images/(?P<path>.*)$', views.serve),
    ]
#urlpatterns = [patterns(
 #   url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT })
    #如果没有建static文件夹，而是直接在根目录下建立的JS,CSS和Images文件夹，就将下面的三行代码注释去掉，删除上方的代码
    #( r'^js/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),
    #( r'^css/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }),
    #( r'^images/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }),
#)