from django.shortcuts import render
from django.http import JsonResponse

from .models import Agreement, Period, Country, Negotiator, Company

def index(request):
    context = {}
    for sm in ('country', 'negotiator', 'company'):
        if request.GET.get(sm)==None:
	    context[sm]=False
	else:
	    context[sm]=[]
    context['empty'] = context.values()==[False]*3

    if request.GET.get('country'):
        for pk in str(request.GET.get('country')).split(','):
	    try:
		context['country'].append(Country.objects.get(id=pk))
	    except Country.DoesNotExist:
		context['country'].append('Country with id=%s does not exist' %s)

    if request.GET.get('negotiator'):
        for pk in str(request.GET.get('negotiator')).split(','):
	    try:
		context['negotiator'].append(Negotiator.objects.get(id=pk))
	    except Negotiator.DoesNotExist:
		context['negotiator'].append('Negotiator with id=%s does not exist' %pk)

    if request.GET.get('company'):
        for pk in str(request.GET.get('company')).split(','):
	    try:
		context['company'].append(Company.objects.get(id=pk))
	    except Company.DoesNotExist:
		context['company'].append('Company with id=%s does not exist' %pk)

    return render(request, 'discount_module/index.html', context)

def agreement_calendar(request):
    agr_calendar = {}
    for agr in Agreement.objects.all():
	if Period.objects.filter(agreement__id=agr.id).exists():
	    per = Period.objects.filter(agreement__id=agr.id).latest('end_date').end_date
	    if per.year not in agr_calendar.keys():
	        agr_calendar[per.year] = [0]*12
	    agr_calendar[per.year][per.month-1] += 1
    return JsonResponse(agr_calendar)

def year_calendar(request, pk):
    context_list = [0]*12
    if Agreement.objects.filter(period__end_date__year=pk).exists():
	agr_ids = []
        for agr in Agreement.objects.filter(period__end_date__year=pk):
            if agr.id not in agr_ids:
		per = Period.objects.filter(agreement__id=agr.id).latest('end_date').end_date
                context_list[per.month-1] += 1
		agr_ids.append(agr.id)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    context = {'year': pk, 'prev': int(pk)-1, 'next': int(pk)+1}
    for m in months:
	context[m] = context_list[months.index(m)]
    return render(request, 'discount_module/year_calendar.html', context)
