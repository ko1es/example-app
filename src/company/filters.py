# -*- coding: utf-8 -*-
"""Company app filters."""
import django_filters

from django.core.validators import EMPTY_VALUES

from company import models


class CompanySearchFilter(django_filters.CharFilter):
    """Company search filter."""

    def filter(self, qs, value):
        """Filter method."""
        if value not in EMPTY_VALUES:
            return qs.search(value)
        return qs


class CompanyRubricFilter(django_filters.NumberFilter):
    """Company rubric filter."""

    def filter(self, qs, value):
        """Filter method."""
        if value not in EMPTY_VALUES:
            return qs.by_rubric(value)
        return qs


class CompanyFilter(django_filters.FilterSet):
    """Company filterset."""

    name = CompanySearchFilter()
    rubric = CompanySearchFilter()

    class Meta:
        """Meta class."""

        model = models.Company
        fields = ['building', 'name', 'rubric']


class RubricFilterSet(django_filters.FilterSet):
    """Rubric filter."""

    class Meta:
        """Meta class."""

        model = models.Rubric
        fields = ['parent', ]
