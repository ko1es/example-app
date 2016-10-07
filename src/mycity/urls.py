# -*- coding: utf-8 -*-
"""Project url config."""
from django.conf.urls import url, include
from django.contrib import admin
from company.views import IndexView, DocumentationView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="app-index"),
    url(r'^api/', include('company.urls', namespace="company-api")),
    url(r'^admin/', admin.site.urls),
    url(r'^documentation.yaml', DocumentationView.as_view(),
        name="yaml-documentation"),
]
