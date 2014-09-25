# -*- coding: utf-8 -*-

# Django imports
from django.db import connection, connections

# import data serializers
import gzip
import csv
import xlrd

# Project imports
from .logger import *


class traverse:
    last = None

    def __call__(self, lst, op):
        for item in lst:
            item = op(item, self.last)
            self.last = item
        return lst


class count:
    ct = 0

    def __call__(lst, comp, op=None):
        for item in lst:
            if(op):
                if(op(item, comp)):
                    self.ct += 1
            else:
                if(item == comp):
                    self.ct += 1
        return self.ct


def find(lst, comp, op=None):
    for item in lst:
        if(op):
            if(op(item, comp)):
                return item
        else:
            if(item == comp):
                return item
    return None


def for_each(lst, op):
    for item in lst:
        item = op(item)
    return lst


def accumulate(lst, op, tgt):
    for item in lst:
        tgt = op(item, tgt)
    return tgt


def propagate(lst, op, tgt1, tgt2):
    for item in lst:
        tgt1, tgt2 = op(item, tgt1, tgt2)
    return tgt1, tgt2


class DataConnector:
    name = 'None'
    #header = None
    head_mapper = None
    current = None
    origin_name = None

    def __init__(self):
        pass

    def __next__(self):
        pass

    def next(self):
        return self.__next__()

    def all(self):
        pass

    def close(self):
        pass


class ExcelConnector(DataConnector):
    fn = None
    sheet_name = None
    sheet = None
    curr_row = 0
    max_row = 0
    header = None

    def __init__(self, fn, sheet_name):
        self. fn = fn
        self.sheet_name = sheet_name
        self.load()

    def __iter__(self):
        return self

    def __next__(self):
        num_rows = self.sheet.nrows - 1
        self.curr_row += 1
        if(self.curr_row < num_rows):
            r = self.sheet.row_values(self.curr_row)
            return dict(list(zip(self.header, r)))
        else:
            raise StopIteration

    def load(self):
        workbook = xlrd.open_workbook(self.fn)
        self.sheet = workbook.sheet_by_name(self.sheet_name)
        self.header = self.get_header()

    def get_header(self):
        return self.sheet.row_values(0)

    def all(self):
        res = []
        for r in self:
            res.append(r)

        return res


class PgsqlConnector(DataConnector):
    cursor = None
    db = None
    header = None
    limit_mode = False
    limit = 10000

    def __init__(self, qry, db=None):
        self.origin_name = qry
        self.db = db
        self.load()

    def __iter__(self):
        return self

    def __next__(self):
        self.current = self.cursor.fetchone()
        if(self.current):
            return dict(list(zip(self.header, self.current)))
        else:
            raise StopIteration

    def load(self):
        if(self.db):
            self.cursor = connections[self.db].cursor()
        else:
            self.cursor = connection.cursor()

        if(self.limit_mode):
            # TODO Add limit functioality
            self.cursor.execute(self.origin_name)
        else:
            self.cursor.execute(self.origin_name)
        self.header = self.get_header()

    def get_header(self):
        return [desc[0] for desc in self.cursor.description]

    def all(self):
        "Returns all rows from a cursor as a dict"
        desc = self.cursor.description
        return [
            dict(list(zip([col[0] for col in desc], row)))
            for row in self.cursor.fetchall()
        ]

    def close(self):
        self.cursor.close()


class CsvConnector(DataConnector):
    reader = None
    f = None
    gzipped = False
    delimiter = ','

    def __init__(self, fn, delimiter=',', gzipped=False):
        Logger.Message("CsvConnector: Loading " + fn)
        self.origin_name = fn
        self.gzipped = gzipped
        self.delimiter = delimiter
        self.load()

    def __iter__(self):
        return self

    def load(self):
        if(self.gzipped):
            self.f = gzip.open(self.origin_name)
        else:
            self.f = open(self.origin_name, 'rb')
        self.reader = csv.DictReader(self.f, delimiter=self.delimiter)
        self.header = self.reader.fieldnames

    def __next__(self):
        self.current = next(self.reader)
        if(self.current):
            return self.current
        else:
            raise StopIteration

    def all(self):
        d = []
        for row in self:
            d.append(row)
        return d

    def close(self):
        self.f.close()


class DictListConnector(DataConnector):

    lst = None

    def __init__(self, lst):
        self.lst = lst
        self.header = list(self.lst[0].keys())
        self.current = iter(self.lst)

    def load(self):
        pass

    def rename(self, row, tgt):

        if not(self.head_mapper):
            return row

        n_row = dict(
            (self.head_mapper[key], value) for (key, value) in list(row.items())
            )

        tgt.append(n_row)
        return tgt

    def reload(self, new_header):
        self.head_mapper = dict(list(zip(self.header, new_header)))
        self.header = new_header
        lst = []
        self.lst = accumulate(self, self.rename, lst)

    def __iter__(self):
        return self

    def __next__(self):
        cur = next(self.current)
        if(cur):
            return cur
        else:
            raise StopIteration

    def all(self):
        return self.lst

    def close(self):
        del self.lst


class DjangoModelConnector(DictListConnector):

    def __init__(self, cls, qry, fields=None):
        if(fields):
            self.lst = list(cls.objects.filter(qry).values(*fields))
        else:
            self.lst = list(cls.objects.filter(qry).values())
        self.header = list(self.lst[0].keys())
        self.current = iter(self.lst)


class DjangoQuerySetConnector(DictListConnector):

    def __init__(self, qs, fields=None):
        if(fields):
            self.lst = list(qs.values(*fields))
        else:
            self.lst = list(qs.values())
        self.header = list(self.lst[0].keys())
        self.current = iter(self.lst)