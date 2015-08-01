#! /usr/bin/env python
#coding=utf-8


import savestockdaily
import csv
import sys,traceback
import os

#savestockdaily.saveAnStockDailyToFile('sh601601','15')
#savestockdaily.saveAnStockDailyToCsvFile('sh601601','15')

stockcodefile = file('stocks_code2.csv', 'rb')
reader = csv.reader(stockcodefile)

try:

    for line in reader:
        print "read:"+line[1]+"["+line[0]+"]"
        # for year in ('06','07','08','09','10','11','12','13','14','15'):
        for year in ('15',):
            #print year
            #savestockdaily.saveAnStockDailyToCsvFile('sh601601',year)
            savestockdaily.saveAnStockDailyToCsvFile(line[0],year)
finally:
    stockcodefile.close();





