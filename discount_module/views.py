from django.shortcuts import render
from django.http import JsonResponse

from .models import Agreement, Period, Country, Negotiator, Company


def agreement_calendar(request):

    periods_all = Period.objects.prefetch_related('agreement')

    periods = []
    set_agr = set(periods_all.values_list('agreement__company__id', flat=True))
    for ind in set_agr:
        period = periods_all.filter(agreement__company__id=ind)
        periods.append(period.latest('end_date'))

    if request.GET:
        filter_list = ['country', 'negotiator', 'company']

        for sm in filter_list:
            try:
                ind = [int(y) for y in str(request.GET.get(sm)).split(',')]
                periods = get_query_filter(sm, ind, periods)
            except ValueError:
                pass

    agr_calendar = {}
    for per in periods:
        if per.end_date.year not in agr_calendar.keys():
            agr_calendar[per.end_date.year] = [0]*12
        agr_calendar[per.end_date.year][per.end_date.month-1] += 1

    return JsonResponse(agr_calendar)


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


# helpfull defs
def get_query_filter(sm, ind, periods):
    if sm == 'country':
        new_periods = [
            x for x in periods if x.agreement.company.country.id in ind
        ]
    if sm == 'negotiator':
        new_periods = [x for x in periods if x.agreement.negotiator.id in ind]
    if sm == 'company':
        new_periods = [x for x in periods if x.agreement.company.id in ind]
    return new_periods
