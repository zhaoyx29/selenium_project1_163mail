# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 17:54
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : writeletters_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class WriteLettersPage:

    def __init__(self,driver):
        self.driver=driver

    #找到收件人输入框，输入收件人
    #找到主题输入框，输入主题
    #上传文件
    #点击发送
    #check-->收件箱
