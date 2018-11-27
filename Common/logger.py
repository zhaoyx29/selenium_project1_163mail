# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 0:15
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : logger.py
import os
import time
import logging
from Common.config_dir import *
from logging.handlers import RotatingFileHandler

#1.定义handler的输出格式
formatter=" %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt="%a, %d %b %Y %H:%M:%S"

#获取当前时间
current_time=time.strftime("%Y-%m-%d %H%M", time.localtime())

#2.输出到控制台，获取handler
sh=logging.StreamHandler()

#3.输出到（log文件）指定文件目录
# fh=logging.FileHandler()
fh=RotatingFileHandler(logs_dir+"/web_autotest_{0}.log".format(current_time),encoding="utf-8")

#4.设置rootlogger 的输出内容形式，输出渠道（基础配置）
logging.basicConfig(format=formatter,datefmt=datefmt,level=logging.INFO,handlers=[sh,fh])
logging.info("163邮箱web测试")