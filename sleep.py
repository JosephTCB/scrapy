from difflib import SequenceMatcher
import json
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# -*- coding: utf-8 -*-
from jieba import posseg
import math
import time
case1 = "个人代开普通发票需要携带哪些资料？"
case2 = "个人代开普通发票所需资料？"
start = time.time()
similarity = similar(case1, case2)
end = time.time()
print(end-start)
print(similarity)
# 对要进行比较的str1和str2进行计算，并返回相似度
def simicos(str1, str2):
    # 对两个要计算的字符串进行分词, 使用隐马尔科夫模型(也可不用)
    # 由于不同的分词算法, 所以分出来的结果可能不一样
    # 也会导致相似度会有所误差, 但是一般影响不大
    # 如果想把所有的词性都计算，那么把if及其后面的全部删除掉即可
    cut_str1 = [w for w, t in posseg.lcut(str1) if 'n' in t or 'v' in t]
    cut_str2 = [w for w, t in posseg.lcut(str2) if 'n' in t or 'v' in t]
    # 列出所有词
    all_words = set(cut_str1 + cut_str2)
    # 计算词频
    freq_str1 = [cut_str1.count(x) for x in all_words]
    freq_str2 = [cut_str2.count(x) for x in all_words]
    # 计算相似度
    sum_all = sum(map(lambda z, y: z * y, freq_str1, freq_str2))
    sqrt_str1 = math.sqrt(sum(x ** 2 for x in freq_str1))
    sqrt_str2 = math.sqrt(sum(x ** 2 for x in freq_str2))
    return sum_all / (sqrt_str1 * sqrt_str2)

if __name__ == '__main__':
    case1 = "个人代开普通发票需要携带哪些资料？"
    case2 = "个人代开普通发票所需资料？"
    start = time.time()
    similarity = simicos(case1, case2)
    end = time.time()
    print("耗时: %.3fs" % (end - start))
    print("相似度: %.3f" % similarity)
# def MergeHost(resource_list):
#         allResource=[]
#         allResource.append(resource_list[0])
#         for dict in resource_list:
#             #print len(l4)
#             k=0
#             for item in allResource:
#                 #print 'item'
#                 if dict['q']!=item['q']:
#                     k=k+1
#                     #continue
#                 else:
#                     break
#                 if k == len(allResource):
#                     allResource.append(dict)
#         taskhost=[]
#         for item in allResource:
#             taskhost.append({'q':item['q'],'a':item['a'],'title':item['title']})
#         return taskhost

# if __name__ == '__main__':
# 	f = open('data.txt','r',encoding='utf-8')  
# 	result = ""
# 	for line in open('data.txt',encoding='utf-8'):  
# 	    line = f.readline()   
# 	    result = result + line 
# 	f.close()
# 	result = result[:-2]
# 	result = "[" + result + "]"
# 	qa = json.loads(result)
# 	qalist = MergeHost(qa)
# 	f = open('data.json','w',encoding='utf-8')
# 	for q_a in qalist:
# 		f.write(json.dumps(q_a,ensure_ascii = False)+',\n')
# 	f.close()