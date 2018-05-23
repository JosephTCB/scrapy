#coding:utf-8
import datetime
str1 = u'2012-11-19'
str2 = u'2018-1-2'
date_time1 = datetime.datetime.strptime(str1,'%Y-%m-%d')
date_time2 = datetime.datetime.strptime(str2,'%Y-%m-%d')
print date_time2
print str1.replace('-','/')
print "   ysudus   ".strip()