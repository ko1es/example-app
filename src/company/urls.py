# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from company import views


urlpatterns = patterns(
    '',
    # building
    url(r'^building/(?P<pk>\d+)/company-list/$',
        views.BuildingCompanies.as_view(), name='building-companies'),
    url(r'^building/list/$',
        views.BuildingList.as_view(), name='building-list'),

    # # Rubric
    url(r'^rubric/(?P<pk>\d+)/company-list/$',
        views.RubricCompanies.as_view(), name='rubric-companies'),
    url(r'^rubric/rubricator/$',
        views.Rubricator.as_view(), name='rubricator'),
    url(r'^rubric/rubricator/(?P<pk>\d+)/$',
        views.Rubricator.as_view(), name='rubricator'),

    # # Company
    url(r'^company/search/$',
        views.CompanySearch.as_view(), name='company-search'),
    url(r'^company/detail/(?P<pk>\d+)/$',
        views.CompanyDetail.as_view(), name='company-detail'),

)
