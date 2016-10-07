# -*- coding: utf-8 -*-
"""Company models."""
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import TemplateModel, CreatedModel, NULLABLE


class BuildingManager(models.Manager):
    """Extended Building model manager."""


class BuildingQuerySet(models.query.QuerySet):
    """Extended QuerySet for Building model."""


class Building(CreatedModel):
    """Building model."""

    address = models.CharField(
        max_length=255, default=None,
        verbose_name=_('address'), **NULLABLE)

    lat = models.IntegerField(
        default=None, verbose_name=_('Latitude'), **NULLABLE)

    lon = models.IntegerField(
        default=None, verbose_name=_('Longitude'), **NULLABLE)

    objects = BuildingManager.from_queryset(BuildingQuerySet)()

    def __str__(self):
        """String method."""
        return self.address

    def __unicode__(self):
        """Unicode method."""
        return self.address

    class Meta:
        """Meta class."""

        verbose_name = _('Building')
        verbose_name_plural = _('Buildings')


class Rubric(TemplateModel):
    """Rubric model."""

    parent = models.ForeignKey(
        "self", default=None, **NULLABLE)

    class Meta:
        """Meta class."""

        verbose_name = _('Rubric')
        verbose_name_plural = _('Rubrics')


class CompanyManager(models.Manager):
    """Extended manager for Company model."""


class CompanyQuerySet(models.query.QuerySet):
    """Extended QuerySet for Company model."""

    def search(self, name):
        """Search company by name."""
        return self.filter(name__icontains=name)

    def by_rubric(self, rubric_id):
        """Search company by rubric."""
        return self.filter(rubrics__rubric__id=rubric_id)

    def all_prefetches(self):
        """Prefetch all related models."""
        return self.prefetch_related('phones', 'rubrics__rubric')

    def all_selections(self):
        """Select all related models."""
        return self.select_related('building')

    def all_relations(self):
        """Prefetch and select related models."""
        return self.all_selections().all_prefetches()


class Company(TemplateModel):
    """Company model."""

    building = models.ForeignKey(Building, verbose_name=_('Building'))

    objects = CompanyManager.from_queryset(CompanyQuerySet)()

    class Meta:
        """Meta class."""

        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class CompanyPhone(CreatedModel):
    """CompanyPhone model."""

    phone = models.CharField(max_length=20, verbose_name=_('Phone'))
    company = models.ForeignKey(
        Company, related_name='phones', verbose_name=_('Company'))

    def __str__(self):
        """String method."""
        return self.phone

    def __unicode__(self):
        """Unicode method."""
        return self.phone

    class Meta:
        """Meta class."""

        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')


class CompanyRubric(CreatedModel):
    """CompanyRubric model."""

    company = models.ForeignKey(
        Company, related_name='rubrics', verbose_name=_('Company'))
    rubric = models.ForeignKey(Rubric, verbose_name=_('Rubric'))

    def __str__(self):
        """String method."""
        return self.rubric.name

    def __unicode__(self):
        """Unicode method."""
        return self.rubric.name

    class Meta:
        """Meta class."""

        verbose_name = _('Company rubric')
        verbose_name_plural = _('Company rubrics')
