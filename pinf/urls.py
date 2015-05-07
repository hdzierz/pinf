from django.conf.urls import patterns, include, url
from django.conf import settings

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
    url(r'^api/(?P<db>[0-9a-zA-Z_]*)/(?P<report>[0-9a-zA-Z_]*)/$', 'web.views.page_api'),
    url(r'^api/(?P<db>[0-9a-zA-Z_]*)/(?P<report>[0-9a-zA-Z_]*)/(?P<qry>[a-z]*)/$', 'web.views.page_api'),
    url(r'^report/(?P<report>[0-9a-zA-Z_]*)/', 'web.views.page_report'),
    url(r'^report/(?P<report>[0-9a-zA-Z_]*)/P<sterm>.*/$', 'web.views.page_report'),
    # url(r'^', 'web.views.page_report_select'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )


