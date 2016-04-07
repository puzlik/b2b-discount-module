from django.contrib import admin

from .models import Negotiator, Country, Company, Period, Agreement

class PeriodInline(admin.TabularInline):
    model = Period

class AgreementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information about Agreement',                      
			            {'fields': [('company', 'negotiator')]}), 
	('Period of Agreement',     {'fields': [('start_date', 'end_date')]}),
	('Amount of export/import', {'fields': ['v_export', 'v_import'],
				     'classes': ['collapse']})
    ]
    inlines = [PeriodInline]

admin.site.register(Agreement, AgreementAdmin)

admin.site.register(Company)

admin.site.register(Country)

admin.site.register(Negotiator)
