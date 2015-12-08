# -*- coding: utf-8 -*-
from rest_framework import serializers

from company import models


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyPhone
        fields = ('phone', )


class ParentRubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rubric
        fields = ('id', 'name')


class RubricSerializer(serializers.ModelSerializer):
    parent = ParentRubricSerializer()

    class Meta:
        model = models.Rubric
        fields = ('id', 'name', 'parent')


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = ('address', 'lat', 'lon')


class CompanySerializer(serializers.ModelSerializer):
    phones = serializers.StringRelatedField(many=True)
    rubrics = serializers.StringRelatedField(many=True)
    building = BuildingSerializer()

    class Meta:
        model = models.Company
        fields = ('id', 'name', 'phones', 'building', 'rubrics')

    # todo: building -> building.address
