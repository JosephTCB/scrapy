# coding=utf-8  
import cx_Oracle   
import json 
f = open('data.txt','r',encoding='utf-8')
content = ''
for line in open('data.txt',encoding='utf-8'):
    line = f.readline()
    content = content + line
f.close()
qa = json.loads(content)
conn=cx_Oracle.connect('YWCL/YWCL@127.0.0.1/ORCL')  
c=conn.cursor()
for q in qa:
    if len(q['a'])<2000:
        try:
            x=c.execute('insert into qa(question,answer) values(:1,:2)',[q['q'],q['a']])
        except:
            print(q['q'])
conn.commit()                
c.close()                                                 
conn.close() 