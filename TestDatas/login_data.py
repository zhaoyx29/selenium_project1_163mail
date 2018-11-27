# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 17:54
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : login_data.py

#成功登录的测试数据
login_success={"username":"18181436390",
               "passwd":"yuqing123456",
               "check":"yuqing.zhao"}


login_error=[
    {"username":"","passwd":"yuqing123456","check":"请输入帐号"},
    {"username":"18181436390","passwd":"","check":"请输入密码"},
    {"username":"181816390","passwd":"yuqing123456","check":"帐号或密码错误"}
]