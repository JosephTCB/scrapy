#coding:utf-8
import xlwt
import json
data=xlwt.Workbook()
table=data.add_sheet(u'知识库',cell_overwrite_ok=True)
f = open('data.txt','r',encoding='utf-8')
result=''
for line in open('data.txt',encoding='utf-8'):
	line = f.readline()
	result = result +line
f.close()
result = result[:-2]
result = "[" + result + "]"
qa = json.loads(result)
i = 0
for q in qa:
	i = i+1
	table.write(i,0,q['q'])
	table.write(i,1,q['a'])
	table.write(i,2,q['title'])
data.save('热点问题.xls')
	
