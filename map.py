#!/usr/local/bin/python

import sys
import csv

class mapper(object):
    def __init__(self, stream):
        self.stream=stream
    def emit(self,key,value1,value2):
        sys.stdout.write('%s%s%s%s%s\n' % (key,str(','),value1,str(','),value2))
    def maps(self):
        data = csv.reader(self.stream)
        for line in data:
            self.emit(line[1],line[4] , line[5])
    


mappers=mapper(sys.stdin)
mappers.maps()