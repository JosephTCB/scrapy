# -*- coding: utf-8 -*-
import json
def MergeHost(resource_list):
	allResource=[]
	allResource.append(resource_list[0])
	for dict in resource_list:
		k = 0
		for item in allResource:
			if dict['q'] != item['q']:
				k = k+1
			else:
				break
			if k == len(allResource):
				allResource.append(dict)
	return allResource

f = open('hnznwd.json','r',encoding='utf-8')  
result = ""
for line in open('hnznwd.json',encoding='utf-8'):  
	line = f.readline()   
	result = result + line 
f.close()
result = result[:-2]
result = "[" + result + "]"
load_dict = json.loads(result)
qalist = MergeHost(load_dict)
file=open('hnznwd.txt','w',encoding='utf-8')
for q_a in qalist:
	content = json.dumps(q_a, ensure_ascii = False) + ',\n'
	file.write(content)  
file.close()
