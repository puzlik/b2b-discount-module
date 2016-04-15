from django.shortcuts import render
from django.http import JsonResponse

from .models import Agreement, Period, Country, Negotiator, Company


def agreement_calendar(request):
    if request.GET == {}:
        agr_calendar = {}
        for per in Period.objects.filter(status=True):
            if per.end_date.year not in agr_calendar.keys():
                agr_calendar[per.end_date.year] = [0]*12
            agr_calendar[per.end_date.year][per.end_date.month-1] += 1
        return JsonResponse(agr_calendar)
    else:
        context = {}
        for sm in ('country', 'negotiator', 'company'):
            if request.GET.get(sm) == None:
                context[sm] = False
            else:
                context[sm] = []
        context['empty'] = context.values() == [False]*3

        if request.GET.get('country'):
            for pk in str(request.GET.get('country')).split(','):
                try:
                    context['country'].append(Country.objects.get(id=pk))
                except Country.DoesNotExist:
                    txt = 'Country with id=%s does not exist' % pk
                    context['country'].append(txt)

        if request.GET.get('negotiator'):
            for pk in str(request.GET.get('negotiator')).split(','):
                try:
                    context['negotiator'].append(Negotiator.objects.get(id=pk))
                except Negotiator.DoesNotExist:
                    txt = 'Negotiator with id=%s does not exist' % pk
                    context['negotiator'].append(txt)

        if request.GET.get('company'):
            for pk in str(request.GET.get('company')).split(','):
                try:
                    context['company'].append(Company.objects.get(id=pk))
                except Company.DoesNotExist:
                    txt = 'Company with id=%s does not exist' % pk
                    context['company'].append(txt)

        return render(request, 'discount_module/calendar.html', context)


def year_calendar(request, pk):
    context_list = [0]*12
    for per in Period.objects.filter(status=True, end_date__year=pk):
            context_list[per.end_date.month-1] += 1

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december']

    context = {'year': pk, 'prev': int(pk)-1, 'next': int(pk)+1}
    for m in months:
        context[m] = context_list[months.index(m)]
    return render(request, 'discount_module/year_calendar.html', context)
