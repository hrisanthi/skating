from django.conf.urls import patterns, url

from skating import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'skating_home'),
        url(r'^athlete/$', views.athleteList, name='skating_athlete_list'),
        url(r'^athlete/(?P<pk>\d+)$', views.athlete, name='skating_athlete'),
        )