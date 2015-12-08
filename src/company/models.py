# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _

from utils.models import TemplateModel, CreatedModel, NULLABLE


class BuildingManager(models.Manager):
    pass


class Building(CreatedModel):
    address = models.CharField(max_length=255,
                               default=None,
                               verbose_name=_('address'),
                               **NULLABLE)

    lat = models.IntegerField(default=None,
                              verbose_name=_('Latitude'),
                              **NULLABLE)
    lon = models.IntegerField(default=None,
                              verbose_name=_('Longitude'),
                              **NULLABLE)

    objects = BuildingManager()

    def __str__(self):
        return self.address

    def __unicode__(self):
        return self.address

    class Meta:
        verbose_name = _('Building')
        verbose_name_plural = _('Buildings')


class Rubric(TemplateModel):
    parent = models.ForeignKey("self",
                               default=None,
                               **NULLABLE)

    class Meta:
        verbose_name = _('Rubric')
        verbose_name_plural = _('Rubrics')


class CompanyManager(models.Manager):
    def get_list(self, building=None, rubric=None,
                 lat=None, lon=None, search=None):
        kwargs = {}
        if building:
            kwargs['building__id'] = building
        if rubric:
            kwargs['rubrics__rubric__id'] = rubric
        if lat:
            kwargs['building__lat__lte'] = lat
        if lon:
            kwargs['building__lon__lte'] = lon
        if search:
            kwargs['name__icontains'] = search
        qs = self
        if kwargs not in EMPTY_VALUES:
            qs = qs.filter(**kwargs)
        qs = qs.prefetch_related('phones', 'rubrics__rubric')
        qs = qs.select_related('building',)
        return qs.distinct()


class Company(TemplateModel):
    building = models.ForeignKey(Building,
                                 verbose_name=_('Building'))

    objects = CompanyManager()

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class CompanyPhone(CreatedModel):
    phone = models.CharField(max_length=20,
                             verbose_name=_('Phone'))
    company = models.ForeignKey(Company,
                                related_name='phones',
                                verbose_name=_('Company'))

    def __str__(self):
        return self.phone

    def __unicode__(self):
        return self.phone

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')


class CompanyRubric(CreatedModel):
    company = models.ForeignKey(Company,
                                related_name='rubrics',
                                verbose_name=_('Company'))
    rubric = models.ForeignKey(Rubric,
                               verbose_name=_('Rubric'))

    def __str__(self):
        return self.rubric.name

    def __unicode__(self):
        return self.rubric.name

    class Meta:
        verbose_name = _('Company rubric')
        verbose_name_plural = _('Company rubrics')
