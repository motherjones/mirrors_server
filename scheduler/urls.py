from django.conf.urls import patterns, url
from scheduler import views

urlpatterns = patterns('reservations.views',
                       url(r'^reservation/$',
                           views.ReservationList.as_view(),
                           name='reservation-list'),
                       url(r'^reservaton/(?P<pk>[0-9]+)/$',
                           views.ReservationDetail.as_view(),
                           name='reservation-detail'),
                       )
