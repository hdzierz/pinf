from nosql.models import *
from api.models import *
import datetime

MAXROWS = 1000000
MAXCOLS = 200


def stop():
    now = datetime.datetime.now()
    print(str(now))


def run():
    stop()

    for i in range(1,MAXROWS):
        if(i%100 == 0):
	    print("Round1 " + str(i))
	vals = {} 
        for j in range(1,MAXCOLS):
            vals['test_' + str(j)] = i*j
	ob = ObKVs()
        ob.name = 'name_' + str(i)
	ob.values = vals
        ob.save()

    stop()

#    for i in range(1,MAXROWS):
#        ob = ObKV()
#	print("Round2 " + str(i))
#        for j in range(1,MAXCOLS):
#            ob.key = 'test_' + str(j)
#            ob.value = str(i * j)
#            ob.save()
#
#    stop()




