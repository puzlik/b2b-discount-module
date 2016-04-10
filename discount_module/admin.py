from django.contrib import admin
from django.contrib.auth.models import User
from .models import Negotiator, Country, Company, Period, Agreement

class PeriodInline(admin.TabularInline):
    model = Period
    ordering = ('start_date', )

class AgreementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information about Agreement',                      
			            {'fields': [('company', 'negotiator')]}), 
	('Period of Agreement',     {'fields': [('start_date', 'end_date')]}),
	('Amount of export/import', {'fields': [('v_export', 'v_import')]})
    ]
    inlines = [PeriodInline]
    list_display = ('company', 'negotiator', 'start_date', 'end_date')
    list_filter = ['company', 'negotiator', 'period__end_date']
    ordering = ['start_date']
    search_fields = ['company__title', 'period__end_date']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'country')
    list_filter = ['country']
    ordering = ['title']
    search_fields = ['title', 'country__name']

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso_code')
    ordering = ['name']
    search_fields = ['iso_code', 'name']

admin.site.register(Agreement, AgreementAdmin)

admin.site.register(Company, CompanyAdmin)

admin.site.register(Country, CountryAdmin)

admin.site.register(Negotiator)
