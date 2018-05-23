import json,re
f = open('hngszymc.json', 'r', encoding='utf-8')
result = ""
for line in open('hngszymc.json', encoding='utf-8'):
	line = f.readline()
	result = result + line
f.close()
result = result[:-2]
result = "[" + result + "]"
load_dict = json.loads(result)

qalist = []
for load in load_dict:
	if(not(load['q'].strip()=='' and load['a'].strip()=='')):
		if(load['a'].find('【业务概述】')!=-1):
			start = load['a'].find('【业务概述】')
			r = re.match(r'^[-0123456789—.]*',load['q']).group()
			q = load['q'].replace(r,'',1).replace(' ','').replace('*','')
			qa = {'q':q,'a':load['a'][start:]}
			qalist.append(qa)
file = open('hngszymc.txt', 'w', encoding='utf-8')
for q_a in qalist:
	content = json.dumps(q_a, ensure_ascii=False) + ',\n'
	file.write(content)
file.close()