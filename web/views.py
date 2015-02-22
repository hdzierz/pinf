from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_tables2_reports.config import RequestConfigReport as RequestConfig
#from django_tables2_reports.utils import create_report_http_response
from django.http import QueryDict, HttpResponse, HttpResponseRedirect
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
    'species': SpeciesTable,
    'primerob': PrimerObTable,
    'markerob': MarkerObTable,
    'default': CityTable,
    }


SEAFOOD_OBJECTS = {
    'fishob': FishOb,
    #'fishobkv': FishObKV,
    'trip': Trip,
    'city': City,
    'crew': Crew,
    'tow': Tow,
    'species': Species,
    'primerob': PrimerOb,
    'markerob': MarkerOb,
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


from django.forms.models import model_to_dict
def expand_values(request, obs):
	from django.forms.models import model_to_dict
	res = []
	for ob in obs:
		buff =  model_to_dict(ob)
		r = {}
		for b in buff:
			if b=='values':
				for v in buff[b]:
				   r[v] = (buff[b][v])
			else:
				r[b] = buff[b]

		res.append(r)
	return res


def get_table1(request, report, config={}):
    try:
        rpt = SEAFOOD_TABLES[report]
        cls = SEAFOOD_OBJECTS[report]

        if config['sterm']:
            obs = cls.objects.filter(obkeywords__contains=config['sterm'])
            return rpt(obs)
        else:
            obs = cls.objects.all()
            return rpt(obs)
    except:
        rpt = SEAFOOD_TABLES['default']
        cls = SEAFOOD_OBJECTS['default']
        return rpt(cls.objects.all())


def get_table(request, report, config={}):
    rpt = SEAFOOD_TABLES[report]
    cls = SEAFOOD_OBJECTS[report]

    try:
        columns = config['cols']
    except:
        columns = 'all'

    if config['sterm']:
        obs = cls.objects.filter(obkeywords__contains=config['sterm'])
    elif request.GET.get('sterm'):
        obs = cls.objects.filter(obkeywords__contains=request.GET.get('sterm'))
    else:
        obs = cls.objects.all()

    fields = []
    values = []

    try:
        fields = []
        values = []
        if(hasattr(obs[0], 'values')):
            vs = obs[0].values
            for k in vs:
                if k in columns or columns == 'all':
                    fields.append(k)
                    values.append(vs[k])
    except:
        pass

    tab = rpt(obs, template = 'table_base.html')
    tab.fields = fields
    tab.values = values
    return tab


def get_queryset(request, report, config=None):
    cls = SEAFOOD_OBJECTS[report]

    if('sterm' in config):
        term = config['sterm']
        return cls.objects.search(term)
    elif('keyw' in config):
        term = config['keyw']
        print term;
        return cls.objects.filter(obkeywords__contains=term)
    else:
        return cls.objects.all()


#@login_required()
def page_report(request, report):
    cfg = {'sterm': ''}
    cols = FishOb.objects.get(name='1').GetColumns()

    if request.method == 'POST':
        flt = FilterForm(request.POST)
        if flt.is_valid() and 'filter' in request.POST:
            cfg['sterm'] = flt.cleaned_data['search']
        else:
            cfg['sterm'] = '' 

        sel = ColumnSelectForm(request.POST, cols) 
        if sel.is_valid():
            columns = sel.cleaned_data['cols']
        else:
            columns = 'all'
    
    else:
        flt = FilterForm()
        cfg['sterm'] = ''
        columns = 'all'

        sel = ColumnSelectForm(cols)

    cfg['cols'] = columns 

    tab = get_table(request, report, cfg)

    for col in tab.base_columns:
        if(col == 'id'):
            tab.base_columns[col].visible = False

    fob = FishOb.objects.get(name=1)
    cols = fob.values.keys()


    RequestConfig(request, paginate={"per_page": 50}).configure(tab)
    return render(
        request,
        "page_report.html",
        {"tab": tab, 'report': report, 'flt': flt, 'sel': sel, 'sterm': cfg['sterm'], 'cols': cols, 'debug': columns}
        )


def page_download(request, report, fmt='csv', conf=None):
    qd = QueryDict(conf)
    conf = qd.dict()

    objs = get_queryset(request, report, conf)
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


def page_columns_select(request):
    
    return render(request, 'page_column_select.html')


def page_report_select(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReportSelectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            report = form.cleaned_data['report']
            return HttpResponseRedirect('/report/' + report  + '/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportSelectForm()

    return render(request, 'page_report_select.html', {'form': form}) 


from django.contrib.auth.models import User

@login_required()
def page_test(request):
    user = User.objects.all()[0] 

    return render(request, 'page_test.html', {'user': user})


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

