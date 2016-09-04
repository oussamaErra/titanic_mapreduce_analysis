#!/usr/bin/local/pyton
import sys
from itertools import groupby
from operator import itemgetter

class reducer(object):
    def __init__(self,stream):
        self.stream= stream
    def __iter__(self):
        for line in self.stream:
            try:
                parts = line.split(',')
                yield parts[0] , parts[1] , float(parts[2])         
            except:
                continue
    def reducers(self):
        for statue , infor in groupby(self,itemgetter(0)):
            list_age =[]
            for x , y , age in infor:
                list_age.append(age)
            self.emit(statue,mean(list_age))
    def mean(a):
        totals=0
        for x in a:
            totals += x
        return totals/len(a) 
    def emit(self,key,value):
        sys.stdout.write('%s%s%s\n'%(key,str(','),value)) 

reduce = reducer(sys.stdin)
reduce.reducers()                                   