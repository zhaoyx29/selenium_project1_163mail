# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 6:27
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : home_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.base_page import BasePage

class HomePage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def get_nickname(self):
        locator_1=(By.XPATH,'//span[@id="spnUid"]')
        self.wait_elevisible(locator_1,15)
        # WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,'//span[@id="1539814535071_dvGreetName"]')))
        get_nickname=self.driver.find_element_by_xpath('//span[@id="spnUid"]')#找到元素用户名昵称
        return get_nickname.text#返回用户名昵称文本信息，后面跟预期值做对比

    def click_writeletters_button(self):#点击写信button，进入写信页面
        locator_2=(By.XPATH,'//li[@class="js-component-component ra0 mD0"]')
        self.wait_elevisible(locator_2,15)
        # WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,'//li[@id="_mail_tabitem_13_220"]')))
        writeletters=self.driver.find_element_by_xpath('//li[@class="js-component-component ra0 mD0"]')
        return writeletters.click()
