# -*- coding: utf-8 -*-
"""Company app views."""
from rest_framework import generics
from django.views.generic import TemplateView


from company import models
from company import serializers


class IndexView(TemplateView):
    """Index view."""

    template_name = 'index.html'


class DocumentationView(TemplateView):
    """Yaml Documentation view."""

    template_name = 'documentation.yaml'

# Api views


class BuildingCompanies(generics.ListAPIView):
    u"""Выдача всех организаций находящихся в конкретном здании."""

    serializer_class = serializers.CompanySerializer
    model = models.Company

    def get_queryset(self):
        """Get queryset method."""
        return models.Company.objects.get_list(
            building=self.kwargs.get('pk', None))


class RubricCompanies(generics.ListAPIView):
    u"""Список всех организаций, которые относятся к указанной рубрике."""

    serializer_class = serializers.CompanySerializer
    model = models.Company

    def get_queryset(self):
        """Get queryset method."""
        return models.Company.objects.get_list(
            rubric=self.kwargs.get('pk', None))


class CompanySearch(generics.ListAPIView):
    u"""Company search resource.

    Список организаций, которые находятся в заданном радиусе/прямоугольной
    области относительно указанной точки на карте.
    поиск организации по названию.
    """

    serializer_class = serializers.CompanySerializer
    model = models.Company
    search_fields = ('name',)

    def get_queryset(self):
        """Get queryset method."""
        lat = None
        lon = None
        if 'lat' in self.request.GET:
            lat = self.request.GET.get('lat', None)
        if 'lon' in self.request.GET:
            lon = self.request.GET.get('lon', None)
        if lat and lon:
            return models.Company.objects.get_list(lat=lat, lon=lon)
        return models.Company.objects.get_list()


class BuildingList(generics.ListAPIView):
    """Building list resource."""

    serializer_class = serializers.BuildingSerializer
    model = models.Building
    queryset = models.Building.objects.all()


class CompanyDetail(generics.RetrieveAPIView):
    u"""Выдача информации об организациях по их идентификаторам."""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    model = models.Company


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
