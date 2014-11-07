# -*- coding: utf-8 -*-


import datetime
from api.connectors import *
from api.imports import *
from api.models import *


class ImportMarkers:
    ds = None
    study = None

    @staticmethod
    def LoadMarkerObsOp(line, succ):
        print(str(line))
        return True

    @staticmethod
    def CleanMarkerObsOp():
        MarkerOb.objects.filter(datasource=ImportMarkers.ds).delete()


def load_markerobs():
    conn = ExcelConnector('data/import/PhenotypesandSamplesHort16AxRussell.xlsx', 'DB_IMPORT')
    im = GenericImport(conn, ImportMarkers.study, ImportMarkers.ds)
    im.load_op = ImportMarkers.LoadMarkerObsOp
    im.clean_op = ImportMarkers.CleanMarkerObsOp
    im.Clean()
    im.Load()



def init():
    dt = datetime.datetime.now()
    ds, created = DataSource.objects.get_or_create(
        name='Initial Import Kiwifruit PSA Markers',
        supplieddate=dt
    )

    st = Study.get_or_create_from_name(
        name='Kiwi',
        species_name='Kiwifruit',
        study_group_name='Kiwifruit',
        study_area_name='Marker Development')

    ImportMarkers.study = st
    ImportMarkers.ds = ds


def run():
    print("Hello")
    init()
    load_markerobs()
