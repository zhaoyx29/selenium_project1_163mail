# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 23:05
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : run.py
import pytest

pytest.main("--html=HtmlTestReport/report.html")
#pytest.main(["-m","demo","--html=HtmlTestReport/report.html"](参数，是一个列表形式)，插件（默认为NONE）)