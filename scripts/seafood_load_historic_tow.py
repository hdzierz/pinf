# -*- coding: utf-8 -*-


from api.connectors import *
from seafood.models import *
from api.imports import *
from os import walk


class Import(ImportOp):
    ob_ct = 0

    @staticmethod
    def LoadDataOp(line, succ):
        sp, created = Species.objects.get_or_create(name=line['Species'])

        if(isinstance(line['Trip Number'], (int, long, float, complex))):
            trip_name = 'Trip_%d' % line['Trip Number']
        else:
            trip_name = 'Trip_%s' % line['Trip Number']
        trip, created = Trip.objects.get_or_create(name=trip_name)

        ob = Tow()
        ob.name = str(line['Tow Number']) 
        ob.recordeddate = datetime.datetime.now()
        ob.trip = trip
        ob.datasource = Import.ds
        ob.study = Import.study
        SaveKVs(ob, line)
        ob.save()

        return True
    
    @staticmethod
    def CleanOp():
        Term.objects.filter(datasource=Import.ds).delete()


def load_tows(fn, sheet):
    conn = ExcelConnector(fn=fn, sheet_name=sheet)
    im = GenericImport(conn, Import.study, Import.ds)
    im.load_op = Import.LoadDataOp
    im.clean_op = Import.CleanOp    
    im.Clean()
    im.Load()


def init(fn, sheet):
    onto = Ontology.objects.get(name="Tow")
    dt = datetime.datetime.now()
    ds, created = DataSource.objects.get_or_create(
        name='Seafood Import Historical Tow Data: ' + fn,
        ontology=onto,
        supplier='Seafood',
    )

    st, created = Study.objects.get_or_create(
        name='Tow Gear'
    )

    Import.study = st
    Import.ds = ds


def run():

    path = 'data/seafood/historic_tow_data/'

    #fn = path + 'COR0045_Towdata.xlsx'

    #sheets = ExcelConnector.GetSheets(fn)
    #init(fn, sheets[0])
    #load_tows(fn, sheets[0])

    for (dirpath, dirname, filenames) in walk(path):
        for fn in filenames:
            fn = path + fn
            print("Processing: " + fn)
            sheets = ExcelConnector.GetSheets(fn)
            init(fn, sheets[0])
            load_tows(fn, sheets[0])

