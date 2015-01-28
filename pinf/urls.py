from django.conf.urls import patterns, include, url

from django.contrib import admin
from web.views import FishObTableView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pinf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^test/', 'web.views.page_test'),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^select_report/', 'web.views.page_report_select'),
    url(r'^select_columns/', 'web.views.page_columns_select'),
    url(r'^api/download/(?P<report>[0-9a-zA-Z_]*)/(?P<fmt>[a-z]*)/$', 'web.views.page_download'),
    url(r'^api/download/(?P<report>[0-9a-zA-Z_]*)/(?P<fmt>[a-z]*)/(?P<conf>.*)/$',
        'web.views.page_download'),
    url(r'^report/(?P<report>[0-9a-zA-Z_]*)/',
        'web.views.page_report'),
    url(r'^report/(?P<report>[0-9a-zA-Z_]*)/P<sterm>.*/$',
        'web.views.page_report'),
    # url(r'^', 'web.views.page_report_select'),
)
