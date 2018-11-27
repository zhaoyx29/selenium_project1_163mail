# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 18:12
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : config_dir.py

import os#引入OS模块

#配置文件，配置文件的目录
#项目顶层目录路径（selenium_project1_163mail）
#print(os.path.realpath(__file__))#获取当前文件路径-->相对路径   os.path.realpath(__file__)->绝对路径
#获取当前文件的上一级目录路径
#print(os.path.split(os.path.realpath(__file__))[0])
#获取最顶层目录路径
base_dir=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#print(base_dir)
#测试数据目录
testdata_dir=os.path.join(base_dir,"TestDatas")
#print(testdata_dir)
#测试用例目录
testcase_dir=os.path.join(base_dir,"TestCases")
#print(testcase_dir)
#截屏文件的路径
screenshot_dir=os.path.join(base_dir,"ScreenShot")
#print(screenshot_dir)
#测试报告的路径
htmlreport_dir=os.path.join(base_dir,"HtmlTestReport")
#print(htmlreport_dir)
#测试日志路径
logs_dir=os.path.join(base_dir,"Logs")
#print(logs_dir)