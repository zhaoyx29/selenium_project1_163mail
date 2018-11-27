# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 8:22
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : login_page_locator.py

from selenium.webdriver.common.by import By

class LoginPageLocator:
    #元素定位
    #iframe 弹框元素定位
    iframe=(By.XPATH,'//iframe[contains(@id,"x-URS-iframe")]')
    #用户名输入框
    user_input=(By.XPATH,'//input[@name="email"]')
    #密码输入框
    # passwd_input='//input[@name="password"]'
    passwd_input=(By.XPATH,'//input[@name="password"]')
    #登录按钮
    # login_button='//a[@id="dologin"]'
    login_button=(By.XPATH,'//a[@id="dologin"]')
    #没有输入用户名,没有密码，用户名格式，密码错误弹框
    # error_prompt_fromloginarea='//div[@id="nerror"]'
    error_prompt_fromloginarea=(By.XPATH,'//div[@id="nerror"]//div[@class="ferrorhead"]')
