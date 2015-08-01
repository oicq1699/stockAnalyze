#! /usr/bin/env python
#coding=utf-8

import urllib
import urllib2
import csv
import re
import sys,traceback
import os

def loadStockDailyFromGtimg(stock_code,year):
    url="http://data.gtimg.cn/flashdata/hushen/daily/"+year+"/"+stock_code+".js"
    print "url="+url
    req=urllib2.Request(url)
    try:
        res_data=urllib2.urlopen(req)
        res_text=res_data.read()
        #print(res_text)
        
        pattern = re.compile(r"""(\d{6})\s{1,3}(\d*\.\d*)
        \s{1,3}(\d*\.\d*)\s{1,3}(\d*\.\d*)
        \s{1,3}(\d*\.\d*)\s{0,3}(\d*)
        """,re.X)
        all_datas=re.findall(pattern,res_text)
        return all_datas
    except Exception,e:
        print e
        #traceback.print_exc() 
        #print sys.exc_info()[0],sys.exc_info()[1]
        print '***********no data!****************'
        return 
    
#保存数据到csv文件
def saveAnStockDailyToCsvFile(stock_code,year):
    #stock_code='sh601601'
    # year="13"
    basepath=os.path.dirname(__file__)
    stockpath=os.path.join(basepath,"stocks")
    if not os.path.exists(stockpath):
        os.mkdir(stockpath)
    
    stock_File=os.path.join(stockpath, stock_code+"_"+year+".csv") 
  
    
    all_datas=loadStockDailyFromGtimg(stock_code,year)
    if(all_datas is None):
        print stock_File+"no data."
        return
    else:
        #csvfile = file(stock_File, 'wb')
        output = open(stock_File, 'wb')
        csvwrite=csv.writer(output)
        try:
            csvwrite.writerows(all_datas)
            #output.writelines(all_datas)
            #z=0
            #for x in all_datas:
              #  trade_date, open_price,close_price,high_price,low_price,volume=x
                #print trade_date, open_price,close_price,high_price,low_price,volume
               # output.write(trade_date+","+open_price+"," \
               # +close_price+","+high_price+","+low_price+","+volume+"\n")
            #raw_input_A = raw_input("raw_input: ")
            print stock_File+"  save success."
        finally:
            output.close(); 


#保存数据到txt文件
def saveAnStockDailyToTxtFile(stock_code,year):
    #stock_code='sh601601'
    # year="13"
    basepath=os.path.dirname(__file__)
    stockpath=os.path.join(basepath,"stocks")
    if not os.path.exists(stockpath):
        os.mkdir(stockpath)
    
    stock_File=os.path.join(stockpath, stock_code+"_"+year+".txt") 
  
    
    all_datas=loadStockDailyFromGtimg(stock_code,year)
    if(all_datas is None):
        print stock_File+"no data."
        return
    else:
        output = open(stock_File, 'w')
        try:
            #output.writelines(all_datas)
            z=0
            for x in all_datas:
                trade_date, open_price,close_price,high_price,low_price,volume=x
                #print trade_date, open_price,close_price,high_price,low_price,volume
                output.write(trade_date+","+open_price+"," \
                +close_price+","+high_price+","+low_price+","+volume+"\n")
            #raw_input_A = raw_input("raw_input: ")
            print stock_File+"data save success."
        finally:
            output.close();    
 
       
     
     
 