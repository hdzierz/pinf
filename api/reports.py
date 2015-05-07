# import data serializers
import tablib
import csv
import re

from django.db import connection

# Project imports
from .models import *
from .logger import *
from api.connectors import *
from .queries import *


class ReportQDict:
    qdict = {}

    def __init__(self):
        pass

    def GetQ(self, nam):
        if nam - self.qdict:
            return qdict[nam]
        else:
            return None

    def RegisterQ(self, nam, q):
        self.qdict[nam] = q


def get_html(result_list):
    return HTML.table(result_list)


def get_csv(result_list):
    import random

    ran = random.randrange(1, 1000000000, 1)

    fn = "nunz_temp_%.10d" % ran

    with open(fn, 'wb') as f:
        w = csv.writer(f)
        w.writerows(result_list)
        f.close()

    with open(fn, 'rb') as f:
        return f.readlines()


def collect_data(row, tgt):
    vals = row.values()
    res = []
    for v in vals:
        res.append(str(v))
    tgt.append(list(res))
    return tgt


def collect_data_with_json(row, tgt):
	vals = row['data']


def collect_data_to_file(row, tgt):
    f.write(','.join(list(row.values())) + "\n")
    return f


class DataProvider:
    fmt = 'csv'
    max_rows = 200000000
    collect_op = collect_data

    @staticmethod
    def ManipulateData(conn, op):
        for_each(conn, op)

    @staticmethod
    def GetData(conn, fmt, conf={}):
        data = tablib.Dataset()
        data.append(conn.header)
        data = accumulate(conn, collect_data, data)

        res = None
        if(fmt == 'json'):
            res = data.json
        elif(fmt == 'csv'):
            res = data.csv
        elif(fmt == 'tab'):
            res = data.tsv
        elif(fmt == 'xls'):
            res = data.xls
        elif(fmt == 'xlsx'):
            res = data.xlsx
        elif(fmt == 'ods'):
            res = data.ods
        elif(fmt == 'yaml'):
            res = data.yaml
        else:
            res = data.html

        return res

    @staticmethod
    def TestQuery(qry):
        qry = "EXPLAIN \n" + qry
        cursor = connection.cursor()
        cursor.execute(qry)
        row = cursor.fetchone()
        m = re.search(r"rows=(\d+)", row[0])

        n_rows_est = int(m.group(1))
        if(n_rows_est > DataProvider.max_rows):
            return 'stopit'

        return 'go'


class Reports:
    queries = reportSQLDict

    def __init__(self):
        pass

    def Register(self, nam, qry):
        if(self.exists(nam)):
            return False
        else:
            self.queries[nam] = qry
            return True

    def Replace(self, nam, qry):
        self.queries[nam] = qry

    def Get(self, name):
        return self.queries[nam]

    def exists(self, nam):
        return nam in self.queries

    def GetData(self, nam, fmt, conf={}):
        if(self.exists(nam)):
            Logger.Message(str(conf))

            if 'limit' in conf:
                conf['limit'] = 'LIMIT ' + conf['limit']
            else:
                conf['limit'] = ''

            qry = self.queries[nam].safe_substitute(conf)

            fn = nam + '.' + fmt

            msg = "Executing query with output " + fn + ":\n" + qry
            Logger.Message(msg)

            conn = PgsqlConnector(qry)

            return DataProvider.GetData(conn, fmt, conf)
        else:
            Logger.Error("ERROR in NunzQuery: Query does not exist")
            raise NunzDataError("ERROR in NunzQuery: Query does not exist")

