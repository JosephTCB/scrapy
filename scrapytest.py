from selenium import webdriver
import time
import requests
driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# bdhandle = driver.current_window_handle
# js = " window.open('http://www.acfun.cn/')" #可以看到是打开新的标签页 不是窗口
# driver.execute_script(js)
# time.sleep(1)
# driver.switch_to_window(bdhandle)
# time.sleep(1)
# handles = driver.window_handles
# driver.switch_to_window(handles[1])
# time.sleep(1)
# driver.get('http://www.sina.com')

driver.get('http://dzhy.ha-n-tax.gov.cn/web/gccx/main_content.htm?GC_DM=1425&RELEASE_DM=2&search_status=0&CLASS_DM=901&current_=2')
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
print(driver.page_source)