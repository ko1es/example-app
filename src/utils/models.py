# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EMPTY_VALUES


NULLABLE = dict(blank=True, null=True)


class EnableException(Exception):
    u'''Исключение объекта на активацию.'''


class DisableException(Exception):
    u'''Исключение объекта на деактивацию.'''


class CreatedModel(models.Model):

    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))

    class Meta:
        abstract = True


class StatusModel(models.Model):

    DISABLED = 0
    ENABLED = 1

    STATUS_CHOICES = (
        (DISABLED, _(u'Не активeн')),
        (ENABLED, _(u'Активен')),
    )

    # TODO: change to ModelChoiceField
    status = models.PositiveSmallIntegerField(verbose_name=_(u'Статус'),
                                              default=ENABLED,
                                              choices=STATUS_CHOICES)

    @property
    def is_active(self):
        return True if self.status == self.ENABLED else False

    def activate(self):
        if self.is_active:
            raise EnableException(_(u'Объект уже активен.'))
        else:
            self.status = self.ENABLED
            self.save()

    def deactivate(self):
        if self.is_active:
            self.status = self.DISABLED
            self.save()
        else:
            raise DisableException(_(u'Объект уже не активен'))

    class Meta:
        abstract = True


class TemplateModel(StatusModel, CreatedModel):

    name = models.CharField(max_length=255,
                            verbose_name=_(u'Название'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


def is_choice_of(status, choices):
    if status in EMPTY_VALUES:
        return False
    for c in choices:
        if c[0] is status:
            return True
    return False
