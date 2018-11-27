# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 17:59
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : test_login_uinttest.py

#测试用例 = 页面对象当中的页面功能 + 测试数据
import unittest
import ddt
from selenium import webdriver
from PageLocators.login_page_locator import LoginPageLocator
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas.login_data import *
from TestDatas.common_data import *

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        #前置条件
        #打开浏览器访问网址
        self.driver=webdriver.Chrome()
        self.driver.get(web_url)
        self.loginpage=LoginPage(self.driver)#调用登陆页面登录方法

   #正常场景用例--登录成功
    def test_login_1_success(self):
        #切换到iframe弹框
        self.loginpage.switch_to_frame(self.loginpage.iframe)

        #用户名，密码，断言：对比数据（yuqing.zhao）
        self.loginpage.login_page(login_success["username"],login_success["passwd"])
        #断言--对比账户名称，确认是否登陆成功
        self.assertEqual(HomePage(self.driver).get_nickname(),login_success["check"])

    #登录失败---ddt修饰相同格式的测试用例（没有用户名，没有密码，用户名或密码格式错误对比时调用函数一样）
    @ddt.data(*login_error)
    def test_login_2_fail(self,data):
         #切换到iframe弹框
        self.loginpage.switch_to_frame(self.loginpage.iframe)
        #用户名，密码，断言：对比数据
        self.loginpage.login_page(data["username"],data["passwd"])
        #断言--对比账户名称，确认是否登陆成功
        self.assertEqual(self.loginpage.get_errormsg_fromloginarea(),data["check"])

    #登录失败--用户名没有注册

    def tearDown(self):
        #后置
        #关闭浏览器
        self.driver.quit()