from django.conf.urls import url

from . import views
app_name = 'films'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^specifics/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<film_id>[0-9]+)/reservation/$', views.reservation, name='reservation'),
]
