"""nairalirayoga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from nairalirayoga.core.views import home, gallery, BlogPost, BlogIndex

urlpatterns = [
    url(r'^$', home),
    url(r'^foto_galeria', gallery),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$', BlogIndex.as_view(), name='index'),
    url(r'^blog/(?P<slug>[\w-]+)/$', BlogPost.as_view(), name='post_detail'),
]

