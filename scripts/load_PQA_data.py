# -*- coding: utf-8 -*-


from api.connectors import *
from api.models_seaf import *
from api.imports import *
import time
import datetime
from django.utils.timezone import get_current_timezone, make_aware


def convert_date(dt):
    return time.strptime(dt, "%d.%m.%Y")


def convert_date_time(dt, default=datetime.datetime.now(), fmt="%d %b %Y  %H:%M:%S"):
    #dt = dt.replace('a.m.', 'AM')
    #dt = dt.replace('p.m.', 'PM')
    tz = get_current_timezone()
    if(dt):
        dt = time.strptime(dt, fmt)
        dt = datetime.datetime.fromtimestamp(time.mktime(dt))
        return make_aware(dt, tz)
    else:
        return make_aware(default, tz)


def convert_boolean(val):
    if val == 'Y':
        return True
    else:
        return False


def convert_int(val):
    try:
        return int(val)
    except Exception:
        return None


class ImportFish(ImportOp):
    ob_ct = 0

    @staticmethod
    def LoadPQAHdrDataOp(line, succ):
        cd = convert_date_time(line['Date Time On Deck'], fmt="%d %b %Y  %H:%M")

        treatment1, created = Treatment.objects.get_or_create(name=line['Treatment 1'])
        treatment2, created = Treatment.objects.get_or_create(name=line['Treatment 2'])
        sm, created = SampleMethod.objects.get_or_create(name=line['Sample Method'])
        ph_instrument, created = Instrument.objects.get_or_create(name=line['PH Instrument'])
        temp_instrument, created = Instrument.objects.get_or_create(name=line['Temp Instrument'])
        twitch_instrument, created = Instrument.objects.get_or_create(
            name=line['Twitch Instrument']
            )
        torry_instrument, created = Instrument.objects.get_or_create(name=line['Torry Instrument'])
        weight_instrument, created = Instrument.objects.get_or_create(
            name=line['Weight Instrument']
            )

        hdr = Tow()
        hdr.createddate = cd
        hdr.city = City.GetByOrigId(line['Townr'])
        hdr.trip = Trip.GetByOrigId(line['Trip'])
        hdr.sample_count = convert_int(line['Sample Count'])
        hdr.sampler = line['Sampler Name']
        hdr.sample_method = sm
        hdr.sample_location = line['Sample Location']
        hdr.no_comment = line['No Comment']
        hdr.comment = line['Comment']
        hdr.external_assessment_only = line['External Assessment Only']
        hdr.study = ImportFish.study
        hdr.datasource = ImportFish.ds
        hdr.save()

        hdr.treatments.add(treatment1)
        hdr.treatments.add(treatment2)
        hdr.instruments.add(ph_instrument)
        hdr.instruments.add(temp_instrument)
        hdr.instruments.add(twitch_instrument)
        hdr.instruments.add(torry_instrument)
        hdr.instruments.add(weight_instrument)

    @staticmethod
    def LoadCrewDataOp(line, succ):
        cd = convert_date_time(line['Date/Time'])
        if not cd:
            cd = datetimne.datetime.now()

        df = convert_boolean(line['Deleted Flag'])

        crew, created = Crew.objects.get_or_create(
            name=line['Crewname'],
            deleted_flag=df
            )

        crew.createddate = cd
        crew.createdby = 'core'
        crew.lastupdatedby = line['Updated By']
        crew.save()

    @staticmethod
    def LoadFishDataOp(line, succ):
        sp, created = Species.objects.get_or_create(name=line['Species'])

        city, created = City.objects.get_or_create(name=line['Townr'], orig_city_id=line['Townr'])

        trip = Trip.objects.get(trip_no=line['Trip'])

        bs, created = BioSubject.objects.get_or_create(
            species=sp,
            name=line['Sample Number']
        )

        fob = FishOb()
        fob.name = ImportFish.ob_ct
        fob.recordeddate = datetime.datetime.now()
        fob.biosubject = bs
        fob.trip = trip
        fob.datasource = ImportFish.ds
        fob.study = ImportFish.study
        fob.form_completed = line['Form Completed Flag']
        fob.city = city
        fob.save()

        fob.SaveKVs(line)

        ImportFish.ob_ct += 1

        return True

    @staticmethod
    def LoadTripDataOp(line, succ):
        sp, created = Species.objects.get_or_create(name=line['Target Species'])

        trip, created = Trip.objects.get_or_create(
            trip_no=line['Trip Number'],
            orig_trip_id=line['Trip Number'],
            species=sp,
            study=ImportFish.study
            )
        if created:
            dd = convert_date_time(line['Date/Time'])
            if not dd:
                dd = datetime.datetime.now()
            trip.createddate = dd
            trip.datasource = ImportFish.ds
            trip.name = 'Trip_' + line['Trip Number']
            trip.study = ImportFish.study
            trip.user = line['User']
            trip.orig_trip_id = line['Trip Number']
            trip.method = line['Fishing Method']
            trip.trip_no = line['Trip Number']
            trip.species = sp
            trip.vessel = line['Vessel Name']
            trip.registration = line['Registration']
            trip.country = 'NZ'
            trip.captain = line['Captain']
            trip.first_sailing = convert_date_time(line['First Sailing Date'])
            trip.last_arrival = convert_date_time(line['Last Arrival Date'])
            trip.deleted = line['Deleted Flag']
            trip.save()
        return True

    @staticmethod
    def CleanOp():
        FishObKV.objects.filter(datasource=ImportFish.ds).delete()
        FishOb.objects.filter(datasource=ImportFish.ds).delete()
        Trip.objects.filter(datasource=ImportFish.ds).delete()

    @staticmethod
    def CleanCrewOp():
        Crew.objects.filter(datasource=ImportFish.ds).delete()

    @staticmethod
    def CleanPQAHdrOp():
        Tow.objects.filter(datasource=ImportFish.ds).delete()


def load_PQA(fn):
    conn = CsvConnector(fn='data/PQAdata.csv', delimiter='|')
    im = GenericImport(conn, ImportFish.study, ImportFish.ds)
    im.load_op = ImportFish.LoadFishDataOp
    im.Load()


def load_trip(fn):
    conn = CsvConnector(fn, delimiter='|')
    im = GenericImport(conn, ImportFish.study, ImportFish.ds)
    im.load_op = ImportFish.LoadTripDataOp
    im.clean_op = ImportFish.CleanOp
    im.Clean()
    im.Load()


def load_crew(fn):
    conn = CsvConnector(fn, delimiter='|')
    im = GenericImport(conn, ImportFish.study, ImportFish.ds)
    im.load_op = ImportFish.LoadCrewDataOp
    im.clean_op = ImportFish.CleanCrewOp
    im.Clean()
    im.Load()


def load_pqa_hdr(fn):
    conn = CsvConnector(fn, delimiter='|')
    im = GenericImport(conn, ImportFish.study, ImportFish.ds)
    im.load_op = ImportFish.LoadPQAHdrDataOp
    im.clean_op = ImportFish.CleanPQAHdrOp
    im.Clean()
    im.Load()


def init():
    dt = datetime.datetime.now()
    ds, created = DataSource.objects.get_or_create(
        name='FishImp Test',
        supplieddate=dt
    )

    st = Study.get_or_create_from_name(
        name='Fish_test',
        species_name='Fish',
        study_group_name='Fish Trips',
        study_area_name='Fish Studies')

    ImportFish.study = st
    ImportFish.ds = ds


def run():
    init()
    load_crew('data/crew.csv')
    load_trip('data/TripData.csv')
    load_pqa_hdr('data/PQAHdr.csv')
    load_PQA('data/PQAdata.csv')
