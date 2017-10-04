from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'results/$', views.ResultsView.as_view(), name='results'),
    url(r'athlete/(?P<name>.+)/$', views.AthleteView.as_view(), name='athlete'),
    url(r'meet/(?P<meetName>.+)/$', views.MeetView.as_view(), name='meet'),
    url(r'team/(?P<teamName>.+)/$', views.TeamView.as_view(), name='team'),
    url(r'all_meets/$', views.AllMeetsView.as_view(), name='allMeets'),





]