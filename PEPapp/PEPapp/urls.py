"""PEPapp URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from PEPapp import settings
from . import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^list/', view.list),
    url(r'^$', view.index),
    url(r'^index/', view.index),
    url(r'^manageApp/', view.manageApp),
    #url(r'^startapp$', view.startapp),
    #url(r'^stopapp$', view.stopapp),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
    url(r'^list/static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}),
]
