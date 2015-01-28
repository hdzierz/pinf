# -*- coding: utf-8 -*-


import datetime
from api.connectors import *
from api.imports import *
from api.models import *


class ImportPrimers:
    ds = None
    study = None

    @staticmethod
    def LoadPrimersOp(line, succ):
        pr = Primer()
        pr.name = line['primerset_id']
        pr.study = ImportPrimers.study
        pr.datasource = ImportPrimers.ds
        pr.save()
        return True

    @staticmethod
    def LoadPrimerObsOp(line, succ):
        print(str(line))
        f_primer = PrimerType.objects.get(name='F_primer')
        r_primer = PrimerType.objects.get(name='R_primer')
    	primer_id = line['primer_id']

        pob = PrimerOb()

        if(primer_id.endswith('F')):
            pid = primer_id.rstrip('F')
            pob.primer, created = Primer.objects.get_or_create(name=pid)
            pob.primer_type = f_primer
        elif(primer_id.endswith('R')):
            pid = primer_id.rstrip('R')
            pob.primer, created = Primer.objects.get_or_create(name=pid)
            pob.primer_type = r_primer
        else:
            pob.primer_type = None
            pob.primer, created = Primer.objects.get_or_create(name=primer_id)

        pob.name = primer_id
        pob.study = ImportPrimers.study
        pob.datasource = ImportPrimers.ds
        pob.sequence = line['primer_sequence']
        pob.tail = line['primer_tail']
        pob.save()
        return True

    @staticmethod
    def CleanPrimersOp():
        Primer.objects.filter(datasource=ImportPrimers.ds).delete()

    @staticmethod
    def CleanPrimerObsOp():
        PrimerOb.objects.filter(datasource=ImportPrimers.ds).delete()


def load_primers():
    qry = "SELECT DISTINCT * FROM primer_set"
    conn = SqlConnector(qry, 'kiwi_marker')
    im = GenericImport(conn, ImportPrimers.study, ImportPrimers.ds)
    im.load_op = ImportPrimers.LoadPrimersOp
    im.clean_op = ImportPrimers.CleanPrimersOp
    im.Clean()
    im.Load()


def load_primerobs():
    qry = "SELECT * FROM primers"
    conn = SqlConnector(qry, 'kiwi_marker')
    im = GenericImport(conn, ImportPrimers.study, ImportPrimers.ds)
    im.load_op = ImportPrimers.LoadPrimerObsOp
    im.clean_op = ImportPrimers.CleanPrimerObsOp
    im.Clean()
    im.Load()



def init():
    dt = datetime.datetime.now()
    ds, created = DataSource.objects.get_or_create(
        name='Initial Import Kiwifruit Primer',
        supplieddate=dt
    )

    st = Study.get_or_create_from_name(
        name='Kiwi',
        species_name='Kiwifruit',
        study_group_name='Kiwifruit',
        study_area_name='Marker Development')

    ImportPrimers.study = st
    ImportPrimers.ds = ds


def run():
    print("Hello")
    init()
    load_primers()
    load_primerobs()
