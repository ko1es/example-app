# -*- coding: utf-8 -*-
"""Company app views."""
from rest_framework import generics
from django.views.generic import TemplateView


from company import models, serializers, filters


class IndexView(TemplateView):
    """Index view."""

    template_name = 'index.html'


class DocumentationView(TemplateView):
    """Yaml Documentation view."""

    template_name = 'documentation.yaml'


# API views

# Company views


class CompanyDetail(generics.RetrieveAPIView):
    u"""Выдача информации об организациях по их идентификаторам."""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    model = models.Company


class CompanyListView(generics.ListAPIView):
    u"""Company list resource.

    Filtering and search available by following parameters:
    - building
    - name
    - rubric
    """

    model = models.Company
    serializer_class = serializers.CompanySerializer
    filter_class = filters.CompanyFilter
    queryset = models.Company.objects.all_relations()


# Building views

class BuildingListView(generics.ListAPIView):
    """Building list resource."""

    serializer_class = serializers.BuildingSerializer
    model = models.Building
    queryset = models.Building.objects.all()


# Rubric views

class Rubricator(generics.ListAPIView):
    u"""Рубрикатор каталога с произвольным уровнем вложенности рубрик друг в друга.

    дерево рубрик каталога со всеми предками, с возможностью фильтрации
    по потомкам конкретного узла
    """

    serializer_class = serializers.RubricSerializer
    model = models.Rubric

    def get_queryset(self):
        """Get queryset method."""
        parent = self.kwargs.get('pk', None)
        if parent:
            return models.Rubric.objects.filter(parent_id=parent)
        return models.Rubric.objects.all()
