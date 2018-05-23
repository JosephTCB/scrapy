# -*- coding: utf-8 -*-  
import json
import re
from operator import itemgetter
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
def MergeHost(resource_list):
	allResource=[]
	allResource.append(resource_list[0])
	for dict in resource_list:
		k = 0
		for item in allResource:
			if dict['q'] != item['q']:
				k = k+1
			else:
            	print(dict)
				break
            if k == len(allResource):
                allResource.append(dict)
    taskhost=[]
    for item in allResource:
        taskhost.append({'q':item['q'],'a':item['a'],'title':item['title']})
    return taskhost

f = open('qa.json','r',encoding='utf-8')  
result = ""
for line in open('qa.json',encoding='utf-8'):  
    line = f.readline()   
    result = result + line 
f.close()
result = result[:-2]
result = "[" + result + "]"
load_dict = json.loads(result)
qa = []
i = 0
for dict in load_dict:
	q_a = dict['qa'].strip()
	if q_a.endswith("？")  or q_a.endswith('?'):
		qa.append({"q":"","a":"","title":""})
		qa[i]["q"] = q_a
		qa[i]["title"] = dict['title'].strip()
		i = i + 1
	else:
		qa[i-1]["a"] = qa[i-1]["a"] + q_a
i = len(qa)
for q in reversed(qa):
	i = i-1
	if (q['q'].find("问：")!=-1 and q['q'].find("答：")!=-1) or q['a'].strip()=="" or (q['a'].find("问：")!=-1 and q['a'].find("答：")!=-1):
		qa.pop(i)
for q in qa:
	try:
		r = re.match(r'^ *(  )*\（?\(?(问题)?[0123456789０１２３４５６７８９一二三四五六七八九十]*\)?\）?[.．、问题：:   ]*'
			,q["q"]).group()
		q["q"] = q["q"].replace(r,'',1)
	except:
		pass
	q['a'] = q['a'].lstrip(r'(回答)?答?:?：?')
f_qa = sorted(qa,key=itemgetter('title'),reverse=True)
qalist = MergeHost(f_qa)
file=open('data.txt','w',encoding='utf-8')
for q_a in qalist:
	content = json.dumps(q_a, ensure_ascii = False) + ',\n'
	file.write(content)  
file.close()
