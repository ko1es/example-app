# -*- coding: utf-8 -*-
from rest_framework import generics
from django.views.generic import TemplateView


from company import models
from company import serializers


class IndexView(TemplateView):
    template_name = 'index.html'


class BuildingCompanies(generics.ListAPIView):
    '''выдача всех организаций находящихся в конкретном здании
    '''
    serializer_class = serializers.CompanySerializer
    model = models.Company

    def get_queryset(self):
        return models.Company.objects.get_list(
            building=self.kwargs.get('pk', None))


class RubricCompanies(generics.ListAPIView):
    ''' список всех организаций, которые относятся к указанной рубрике
    '''
    serializer_class = serializers.CompanySerializer
    model = models.Company

    def get_queryset(self):
        return models.Company.objects.get_list(
            rubric=self.kwargs.get('pk', None))


class CompanySearch(generics.ListAPIView):
    '''список организаций, которые находятся в заданном радиусе/прямоугольной
    области относительно указанной точки на карте.
    поиск организации по названию.
    '''
    serializer_class = serializers.CompanySerializer
    model = models.Company
    search_fields = ('name',)

    def get_queryset(self):
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
    '''список зданий
    '''
    serializer_class = serializers.BuildingSerializer
    model = models.Building

    def get_queryset(self):
        return models.Building.objects.all()


class CompanyDetail(generics.RetrieveAPIView):
    '''выдача информации об организациях по их идентификаторам
    '''
    serializer_class = serializers.CompanySerializer
    model = models.Company

    def get_queryset(self):
        return models.Company.objects.all()


class Rubricator(generics.ListAPIView):
    '''рубрикатор каталога сделать с произвольным уровнем вложенности рубрик
     друг в друга.
     дерево рубрик каталога со всеми предками, с возможностью фильтрации
    по потомкам конкретного узла
    '''
    serializer_class = serializers.RubricSerializer
    model = models.Rubric

    def get_queryset(self):
        parent = self.kwargs.get('pk', None)
        if parent:
            return models.Rubric.objects.filter(parent_id=parent)
        return models.Rubric.objects.all()
