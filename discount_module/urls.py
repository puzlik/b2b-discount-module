from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^agreements/calendar/$', views.agreement_calendar, name='calendar'),
    url(r'^agreements/calendar/(?P<pk>[0-9]+)/$', views.year_calendar, name='year-calendar'),
]
