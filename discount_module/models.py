import datetime

from django.contrib.auth.models import User
from django.db import models


class Negotiator(models.Model):
    negotiator = models.ForeignKey(User)
    def __str__(self):
        return self.negotiator.username


class Country(models.Model):
    iso_code = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    def __str__(self):
        return self.title


class Agreement(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.ForeignKey(Company)
    negotiator = models.ForeignKey(Negotiator)
    v_export = models.IntegerField()
    v_import = models.IntegerField()
    def __str__(self):
        return '%s - %s (%s)' %(self.start_date, self.end_date, self.company)


class Period(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    agreement = models.ForeignKey(Agreement)
    def status_of_period(self):
        return self.end_date <= datetime.today()
    def __str__(self):
        return '%s - %s' %(self.start_date, self.end_date)
