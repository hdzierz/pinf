from django.shortcuts import render
from django_tables2_reports.config import RequestConfigReport as RequestConfig
#from django_tables2_reports.utils import create_report_http_response
from django.http import QueryDict, HttpResponse
from api.connectors import *
from api.reports import *
from .forms import *
#from django_tables2 import *


from api.models import *
from .tables import *


SEAFOOD_TABLES = {
    'fishob': FishObTable,
    'trip': TripTable,
    'city': CityTable,
    'crew': CrewTable,
    'tow': TowTable,
    'default': CityTable,
    }


SEAFOOD_OBJECTS = {
    'fishob': FishOb,
    'fishobkv': FishObKV,
    'trip': Trip,
    'city': City,
    'crew': Crew,
    'tow': Tow,
    'default': City,
    }


def get_mime_type(ext):
    if(ext == 'json'):
        return 'Content-type: application/json', False

    elif(ext == 'xml'):
        return 'Content-type: application/xml', False

    elif(ext == 'yaml'):
        return 'Content-type: text/x-yaml', False

    elif(ext == 'csv'):
        return 'Content-type: text/csv', False

    elif(ext == 'gzip'):
        return 'Content-type: application/x-gzip', True

    return 'Content-type: application/octet-stream', True


def get_table(request, report, config={}):
    try:
        rpt = SEAFOOD_TABLES[report]
        cls = SEAFOOD_OBJECTS[report]
        if config['sterm']:
            return rpt(cls.objects.filter(obkeywords__contains=config['sterm']))
        else:
            return rpt(cls.objects.all())
    except:
        rpt = SEAFOOD_TABLES['default']
        cls = SEAFOOD_OBJECTS['default']
        return rpt(cls.objects.all())


def get_queryset(request, report, config={}):
    cls = SEAFOOD_OBJECTS[report]
    return cls.objects.all()


#@login_required()
def page_report(request, report):
    cfg = {'sterm': None}
    if request.method == 'POST':
        flt = FilterForm(request.POST)
        if flt.is_valid():
            cfg['sterm'] = flt.cleaned_data['search']
        else:
            cfg['sterm'] = None
    else:
        flt = FilterForm()
        cfg['sterm'] = None

    tab = get_table(request, report, cfg)

    for col in tab.base_columns:
        if(col == 'id'):
            tab.base_columns[col].visible = False

    RequestConfig(request, paginate={"per_page": 50}).configure(tab)
    return render(
        request,
        "page_report.html",
        {"tab": tab, 'report': report, 'flt': flt}
        )


def page_download(request, report, fmt='csv'):
    objs = get_queryset(request, report)
    if not objs:
        return HttpResponse('No Data')

    conn = DjangoQuerySetConnector(objs)
    data = DataProvider.GetData(conn, fmt)
    if data:
        c_type, download = get_mime_type(fmt)
        fn = report + "." + fmt
        response = HttpResponse(data, content_type=c_type)
        if(download):
            response['Content-Disposition'] = 'attachment; filename="' + fn + '"'
        return response
    else:
        response = HttpResponse('Report does not exist')
        return response


from django_tables2 import SingleTableView
from web.filters import *


class PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(PagedFilteredTableView, self).get_table()
        RequestConfig(self.request, paginate={'page': self.kwargs['page'],
                            "per_page": self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


from crispy_forms.helper import FormHelper


class FishObTableView(PagedFilteredTableView):
    model = FishOb
    table_class = FishObTable
    template_name = 'page_test.html'
    paginate_by = 50
    filter_class = FishObFilter
    formhelper_class = FormHelper


