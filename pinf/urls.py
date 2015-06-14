from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from genotype.views import MarkerView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pinf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', 'genotype.views.test_dict'),
    url(r'^test2/(?P<pk>[0-9]*)$', MarkerView.as_view(), name='marker-detail'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^select_report/', 'web.views.page_report_select'),
    url(r'^select_columns/', 'web.views.page_columns_select'),
    url(r'^api/(?P<report>[0-9a-zA-Z_]*)/(?P<pk>[0-9]+)$', 'genotype.views.restfully_manage_element'),
    url(r'^api/(?P<report>[0-9a-zA-Z_]*)/(?P<qry>[0-9a-zA-Z_\.]*)$', 'genotype.views.restfully_manage_collection'),
    url(r'^report/(?P<db>[0-9a-zA-Z_]*)/(?P<report>[0-9a-zA-Z_]*)/$', 'web.views.page_api'),
    url(r'^report/(?P<db>[0-9a-zA-Z_]*)/(?P<report>[0-9a-zA-Z_]*)/(?P<fmt>[a-z]*)/$', 'web.views.page_api'),
    #url(r'^test/marker/$', 'genotype.views.MarkerView.as_view()', name='marker_list'),
    # url(r'^', 'web.views.page_report_select'),
)

if settings.DEBUG and False:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )


