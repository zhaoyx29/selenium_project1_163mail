# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 16:23
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : iframe.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
time.sleep(0.5)
driver.get('https://email.163.com')

locator='//iframe[contains(@id,"x-URS-iframe")]'
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,locator)))
driver.switch_to.frame(driver.find_element_by_xpath(locator))

driver.find_element_by_xpath('//input[@name="email"]').send_keys('18181436390')

time.sleep(0.5)
driver.quit()




