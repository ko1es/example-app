# -*- coding: utf-8 -*-
"""Pagination settings."""

from rest_framework.pagination import PageNumberPagination


class ExamplePagination(PageNumberPagination):
    """Pagination settings class."""

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
