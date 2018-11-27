# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 6:52
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : login_page.py
from PageLocators.login_page_locator import LoginPageLocator
from Common.base_page import BasePage


class LoginPage(LoginPageLocator,BasePage):#继承元素定位类,BasePage类

    def login_page(self,username,passwd):#登录页面的登录成功方法
        #日志内容：登录页面的登录功能
        name="登录页面的登录功能"
        # self.switch_to_frame(self.iframe,model=name)#等待iframe弹框出现
        self.wait_elevisible(self.user_input,model=name)#等待用户名输入框出现
        self.input_text(self.user_input,username,model=name)#定位到用户名输入框，输入用户名
        self.input_text(self.passwd_input,passwd,model=name)#定位到密码输入框，输入密码
        self.click_element(self.login_button,model=name)#定位到登录按钮，执行点击操作函数

    def get_errormsg_fromloginarea(self):#登录页面的登陆失败方法
        #日志内容：登录页面登陆失败的提示
        name="登录页面登录失败的提示"
        # self.switch_to_frame(self.iframe,model=name)#等待iframe弹框出现
       #提示用户名，密码错误/没有的弹出框
        self.wait_elevisible(self.error_prompt_fromloginarea)
        return self.get_text(self.error_prompt_fromloginarea,model=name)#返回文本信息，testcase里做比对用


    def register(self):#注册方法
        pass