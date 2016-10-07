# -*- coding: utf-8 -*-
"""Company app filters."""
import django_filters

from django.core.validators import EMPTY_VALUES

from company.models import Company


class CompanySearchFilter(django_filters.NumberFilter):
    """Company search filter."""

    def filter(self, qs, value):
        """Filter method."""
        if value not in EMPTY_VALUES:
            # TODO: check value is category id
            return qs.filter(companysubcategory__subcategory__id=value)
        return qs


class CompanyFilter(django_filters.FilterSet):
    """Company filter."""

    coordinates = CompanySearchFilter()

    class Meta:
        """Meta class."""

        model = Company
        fields = ['coordinates', ]
