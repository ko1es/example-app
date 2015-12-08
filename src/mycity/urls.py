# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from company.views import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="app-index"),
    url(r'^api/', include('company.urls', namespace="company-api")),
    url(r'^admin/', admin.site.urls),
]