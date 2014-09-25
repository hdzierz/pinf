from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pinf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/report/(?P<report>[0-9a-zA-Z_]*)/(?P<fmt>[a-z]*)/$',
        'web.views.page_download'),
    url(r'^api/report/(?P<report>[0-9a-zA-Z_]*)/(?P<fmt>[a-z]*)/(?P<conf>.*)/$',
        'web.views.page_download'),
    url(r'^report/(?P<report>[0-9a-zA-Z_]*)/',
        'web.views.page_report'),
)
