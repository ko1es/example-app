# -*- coding: utf-8 -*-
"""Company url config."""
from django.conf.urls import url

from company import views


urlpatterns = [
    # building
    url(r'^building/$',
        views.BuildingListView.as_view(), name='building-list'),
    # # Rubric
    url(r'^rubric/rubricator/$',
        views.Rubricator.as_view(), name='rubricator'),
    url(r'^rubric/rubricator/(?P<pk>\d+)/$',
        views.Rubricator.as_view(), name='rubricator'),
    # # Company
    url(r'^company/$',
        views.CompanyListView.as_view(), name='company-list'),
    url(r'^company/(?P<pk>\d+)/$',
        views.CompanyDetail.as_view(), name='company-detail'),
]
