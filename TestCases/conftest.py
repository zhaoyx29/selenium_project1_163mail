# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 19:52
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : conftest.py
import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
#测试数据
from TestDatas.login_data import  *
from TestDatas import common_data
from Common import logger
from Common.logger import *

#登陆用例的前置 和后置
#setup 和teardown
@pytest.fixture
def init_loginEnv():#定义一个函数，在这个函数当中，实现用例的准备工作和清理工作 在函数前加@pytest.fixture  fixture可以设置作用域范围
    #前置  初始化浏览器会话
    logging.info("用例前的准备工作")
    option=webdriver.ChromeOptions()
    option.add_argument('headless')
    driver=webdriver.Chrome(chrome_options=option)
    driver.maximize_window()
    driver.get(common_data.web_url)
    loginpage=LoginPage(driver)#调用登录页面的登陆方法
    #yield 准备工作和清理工作的分限线。上面是准备工作。下面的是清理工作
    #有返回值的情况下，返回值写在yield后面。
    loginpage.switch_to_frame(loginpage.iframe)
    yield [driver,loginpage]#返回值是init_loginEnv（）接收的
    #后置 关闭浏览器
    driver.quit()