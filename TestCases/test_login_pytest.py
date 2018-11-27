# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 7:16
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : test_login_pytest.py

import pytest
from PageObjects.home_page import HomePage
from TestDatas import login_data
from Common.logger import *
from PageLocators.login_page_locator import LoginPageLocator

@pytest.mark.usefixtures("init_loginEnv")
class TestLogin:
   #正常场景用例--登录成功
   #init_loginEnv(fixture函数名称)接收 fixture运行的返回值  [driver,loginpage]
    def test_login_success(self,init_loginEnv):
        #切换到iframe弹框
        #init_loginEnv[1].switch_to_frame(LoginPageLocator.iframe)

        #用户名，密码，断言：对比数据（yuqing.zhao）
        init_loginEnv[1].login_page(login_data.login_success["username"],login_data.login_success["passwd"])
        #断言--对比账户名称，确认是否登陆成功
        try:
            assert HomePage(init_loginEnv[0]).get_nickname()==login_data.login_success["check"]
        except AssertionError:
            logging.exception("断言失败")
            raise

    @pytest.mark.parametrize("data",login_data.login_error)
    def test_login_2_fail(self,init_loginEnv,data):

        #init_loginEnv[1].switch_to_frame(LoginPageLocator.iframe)
       #用户名，密码，断言：对比数据
        init_loginEnv[1].login_page(data["username"],data["passwd"])
        #断言--对比账户名称，确认是否登陆成功
        try:
            assert init_loginEnv[1].get_errormsg_fromloginarea()==data["check"]
        except AssertionError:
            logging.info("断言失败")
            raise
