from django.conf.urls import patterns, include, url
from mirrors import urls as mirrors_urls
from scheduler import urls as scheduler_urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mirrors_server.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^mirrors/', include(mirrors_urls)),
                       url(r'^scheduler/', include(scheduler_urls)),
                       url(r'^admin/', include(admin.site.urls)),
                  )
