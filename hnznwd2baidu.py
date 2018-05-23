import json
f = open('hnznwd.txt','r',encoding='utf-8')
result=''
for line in open('data.txt',encoding='utf-8'):
	line = f.readline()
	result = result + line
f.close()
result = result[:-2]
result = "[" + result + "]"
qa = json.loads(result)
i = 0
content = ''
for q in qa:
	if i < 2000:
		if len(q['q']) < 100 and len(q['a']) < 1000:
			content = content + q['q'] + '\t' + q['a'] + '\r'
	i = i +1
file=open('hn2baidu.txt','w',encoding='utf-8')
file.write(content)  
file.close()