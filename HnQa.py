# coding: utf-8
import scrapy
from scrapy import Spider
import json, time
from bs4 import BeautifulSoup
from scrapy.http import Request
from selenium import webdriver
import datetime

class HnQaSpider(Spider):
	name = 'qa'
	allowed_domains = ['218.28.41.134']
	start_urls = ['http://218.28.41.134//hnww/FullTextSearchBLH_searchMain.do#']

	def parse(self, response):
		url = 'http://218.28.41.134//hnww/FullTextSearchBLH_searchMain.do#'
		driver = webdriver.Chrome()
		driver.get(url)
		driver.find_element_by_id('id2').click()
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		while soup.select('div#menunav_2.menucon') == []:
			time.sleep(5)
			print('我是输出',soup.select('div#menunav_2.menucon'))
		node_list = soup.select('div#menunav_2.menucon')[0].select('ul')
		for node in node_list:
			print(node.li.s.span.get_text())
		# while driver.page_source.find('default_pgNextDisabled') == -1:
			# soup = BeautifulSoup(driver.page_source, 'html.parser')
			# node_list = soup.select('div.title_list.font15_wryh')[0].select('a')
			# yield Request(url=href, callback=self.find_parse)
			# kepp_request = True
			# while kepp_request:
				# try:
					# driver.find_element_by_class_name('default_pgNext').click()
					# kepp_request = False
				# except:
					# print(u'重新连接...')
					# time.sleep(1)
			# i = i + 1

	def find_parse(self, response):
		pass
		# node_list = response.xpath('//div[@id="contentText"]/p')
		# content = ''
		# for node in node_list:
			# li = node.xpath('string(.)').extract()[0].split('\r\n')
			# for l in li:
				# if l.strip()!='':
					# q = {'qa': ''}
					# q['qa'] =l
					# content = content + json.dumps(q, ensure_ascii=False) + ',\n'
		# file = open('qa.json', 'a',encoding='utf-8')
		# file.write(content)
		# file.close()
