# -*- coding: utf-8 -*-
"""Company app serializers."""
from rest_framework import serializers

from company import models


class PhoneSerializer(serializers.ModelSerializer):
    """Phone views serializer."""

    class Meta:
        """Meta class."""

        model = models.CompanyPhone
        fields = ('phone', )


class ParentRubricSerializer(serializers.ModelSerializer):
    """ParentRubric serializer."""

    class Meta:
        """Meta class."""

        model = models.Rubric
        fields = ('id', 'name')


class RubricSerializer(serializers.ModelSerializer):
    """Rubric serializer."""

    parent = ParentRubricSerializer()

    class Meta:
        """Meta class."""

        model = models.Rubric
        fields = ('id', 'name', 'parent')


class BuildingSerializer(serializers.ModelSerializer):
    """Building serializer."""

    class Meta:
        """Meta class."""

        model = models.Building
        fields = ('address', 'lat', 'lon')


class CompanySerializer(serializers.ModelSerializer):
    """Company serializer."""

    phones = serializers.StringRelatedField(many=True)
    rubrics = serializers.StringRelatedField(many=True)
    building = BuildingSerializer()

    class Meta:
        """Meta class."""

        model = models.Company
        fields = ('id', 'name', 'phones', 'building', 'rubrics')
