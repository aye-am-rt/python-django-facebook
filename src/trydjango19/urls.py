"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


A list of common regular expressions for use in django url's regex.

Example Django URLs patterns:

from django.conf.urls import url, include
# Django 1.9 and Up (required in Django 1.10+)
# urls.py

from django.conf.urls import url, include
from appname.views import (
              AboutView,
              article_detail, 
              ContactView,
              home_view, 
              profile_detail,
              )


urlpatterns = [
    # Examples:
    url(r'^$', home_view, name='home'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', profile_detail, name='profile'),
    url(r'^article/(?P<slug>[\w-]+)/$', article_detail, name='article'),
    url(r'^blog/', include("blog.urls")),
    url(r'^admin/', admin.site.urls),
]


# Django 1.8 and below
# urls.py
from appname.views import (
              AboutView,
              ContactView,
              )
              
              
urlpatterns = patterns('',
    url(r'^$', 'appname.views.home_view', name='home'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', 'appname.views.profile_detail', name='about'),
    url(r'^article/(?P<slug>[\w-]+)/$', 'appname.views.article_detail', name='about'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
    # include((appname.urls, app_name), namespace='any_name'))
    url(r'^posts/', include(('posts.urls', 'posts'), namespace='posts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

