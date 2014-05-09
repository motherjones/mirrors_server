from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from scheduler import views

urlpatterns = patterns('reservations.views',
                       url(r'^schedule/$', views.ReservationList.as_view()),
                       url(r'^schedule/(?P<pk>[0-9]+)/$', views.ReservationDetail.as_view()),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
