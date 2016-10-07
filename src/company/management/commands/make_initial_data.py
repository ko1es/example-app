# -*- coding: utf-8 -*-
"""Create admin command."""
from random import randint
from django.core.management.base import BaseCommand

from company import models


class Command(BaseCommand):
    """Command."""

    help = 'Make data init'

    def handle(self, *args, **options):
        """Handle method."""
        # make rubrics
        rubrics = list()
        for r in range(1, 10):
            rubrics.append(models.Rubric(name='Rubric_%d' % r,))
        models.Rubric.objects.bulk_create(rubrics)
        # make rubrics with parents
        randomrubric_qs = models.Rubric.objects.order_by('?')
        subrubrics = list()
        for s in range(1, 10):
            parent = randomrubric_qs.first()
            subrubrics.append(
                models.Rubric(
                    name='Rubric_%d_%d' % (parent.id, s),
                    parent=parent)
            )
        models.Rubric.objects.bulk_create(subrubrics)
        # make buildings
        buildings = list()
        for b in range(1, 3):
            buildings.append(
                models.Building(
                    address='building_adress_%d' % b,
                    lat=randint(0, 100), lon=randint(0, 100))
            )
        models.Building.objects.bulk_create(buildings)
        # make 10 companies
        companies = list()
        randombuilding_qs = models.Building.objects.order_by('?')
        for c in range(1, 10):
            building = randombuilding_qs.first()
            companies.append(
                models.Company(name='Company_%d' % c, building=building)
            )
        models.Company.objects.bulk_create(companies)
        # make CompanyPhones
        phones = list()
        for company in models.Company.objects.all():
            for x in range(0, randint(0, 2)):
                phones.append(models.CompanyPhone(
                    company=company,
                    phone='%d' % randint(79000000000, 79999999999)
                ))
        models.CompanyPhone.objects.bulk_create(phones)
        # make CompanyRubric
        companyrubrics = list()
        for company in models.Company.objects.all():
            for rr in randomrubric_qs[0:randint(0, 2)]:
                companyrubrics.append(
                    models.CompanyRubric(company=company, rubric=rr)
                )
        models.CompanyRubric.objects.bulk_create(companyrubrics)
        message = 'Initial data successfully created'
        self.stdout.write(self.style.SUCCESS(message))
