# -*- coding: utf-8 -*-
import django_filters

from django.core.validators import EMPTY_VALUES

from company.models import Company


class CompanySearchFilter(django_filters.NumberFilter):
    def filter(self, qs, value):
        import ipdb; ipdb.set_trace()
        if value not in EMPTY_VALUES:
            # TODO: check value is category id
            return qs.filter(companysubcategory__subcategory__id=value)
        return qs


class CompanyFilter(django_filters.FilterSet):
    coordinates = CompanySearchFilter()

    class Meta:
        model = Company
        fields = ['coordinates', ]
