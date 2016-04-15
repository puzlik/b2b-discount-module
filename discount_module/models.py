import datetime

from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


class Negotiator(models.Model):
    negotiator = models.ForeignKey(User)

    def __str__(self):
        return self.negotiator.username


class Country(models.Model):
    iso_code = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50)
    verbose_name_plural = "countries"

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=100)
    country = models.ForeignKey(Country)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.title


class Agreement(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.ForeignKey(Company)
    negotiator = models.ForeignKey(Negotiator)
    v_export = models.IntegerField(blank=True)
    v_import = models.IntegerField(blank=True)

    def __str__(self):
        return '%s - %s (%s)' % (self.start_date, self.end_date, self.company)


class Period(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(blank=True, editable=False, default=False)
    agreement = models.ForeignKey(Agreement)

    def clean(self):
        if (self.start_date < self.agreement.start_date) \
         or (self.end_date > self.agreement.end_date):
            raise ValidationError('Period is outside of the agreement')

    # periods don't intersect
        objs = self.__class__.objects
        periods = objs.filter(agreement__id=self.agreement.id)
        if periods.exists():
            for per in periods:
                if not per == self:
                    if per.end_date >= self.start_date >= per.start_date \
                     or per.end_date >= self.end_date >= per.start_date:
                        txt = 'Period intersects with an existing period'
                        raise ValidationError(txt)

    def __str__(self):
        return '%s - %s (%s)' \
          % (self.start_date, self.end_date, self.agreement.company)

    def set_status(self):  # auto set status
        agrs = self.__class__.objects.filter(agreement__id=self.agreement.id)
        if self.end_date == agrs.latest('end_date').end_date:
            for obj in self.__class__.objects.filter(status=True):
                obj.status = False
                obj.save()
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        super(Period, self).save(*args, **kwargs)
        self.status = self.set_status()
        super(Period, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.status is True:
            super(Period, self).delete(*args, **kwargs)
            objss = self.__class__.objects
            objs = objs.filter(agreement__id=self.agreement.id)
            obj = objs.latest('end_date')
            obj.status = True
            obj.save()
        else:
            super(Period, self).delete(*args, **kwargs)
