# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 6:55
# @Author  :  'zyq'
# @Email   :  : 865281359@qq.com
# @File    : base_page.py


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.logger import *

class BasePage:
      def __init__(self,driver):#定义driver
        self.driver=driver

      #等待元素可见 若失败，有截图有日志
      def wait_elevisible(self,locator,wait_time=20,poll_frequency=0.5,model=""):
        """
        :param locator: 类型为元组(By.XXX,定位表达式)
        :return:
        """
        try:
            logging.info("等待操作")
            WebDriverWait(self.driver,wait_time,poll_frequency).until(EC.visibility_of_element_located(locator))#等待元素可见，此处可以传入元组形式
        except:
            #捕获异常到日志中
            logging.exception("等待元素可见：")
            #截图---保存到的指定的目录
            self._screenshot(model)
#            #抛出异常
            raise

        #查找元素
      def get_element(self,locator,model=""):
          try:
             logging.info("查找元素")
             ele=self.driver.find_element(locator[0],locator[1])
             return ele
          except:
              #捕获异常到日志中
              logging.exception("查找元素失败：")
              #截图
              self._screenshot(model)
              #抛出异常
              raise

        #输入操作
      def input_text(self,locator,text,model=""):
          #找到元素
          ele=self.get_element(locator)
          #输入操作
          try:
              ele.send_keys(text)
          except:
              #捕获异常到日志中
              logging.exception("输入操作失败：")
              #截图
              self._screenshot(model)
              #抛出异常
              raise

        #点击按钮
      def click_element(self,locator,model=""):
          #找到元素(点击按钮得元素定位)
          ele=self.get_element(locator)
          #点击操作
          try:
              ele.click()
          except:
              #捕获异常到日志中
              logging.exception("点击操作失败：")
              #截图
              self._screenshot(model)
              #抛出异常
              raise

        #获取元素属性
      def get_element_attribute(self,locator,attr_name,model=""):
          #找到元素(点击按钮的元素定位)
          ele=self.get_element(locator)
          # 获取元素的属性
          try:
              attr=ele.get_attribute(attr_name)
              return attr#返回属性
          except:
              #捕获异常到日志中
              logging.exception("获取元素属性失败：")
              #截图
              self._screenshot(model)
              #抛出异常
              raise

        #获取元素的文本
      def get_text(self,locator,model=""):
           #找到元素(点击按钮得元素定位)
           ele=self.get_element(locator)
           #获取元素的文本
           try:
               text=ele.text
               return text
           except:
               #捕获异常到日志中
               logging.exception("获取元素的文本内容失败：")
               #截图
               self._screenshot(model)
               #抛出异常
               raise

        #截图操作
      def _screenshot(self,model_name):#加_是私有函数，表明函数只在此文件内使用（其他文件也可以调用的）
          filepath=screenshot_dir+"/{0}_{1}.png".format(model_name,time.strftime("%Y%m%d_%H%M%S"))#时间格式
          self.driver.save_screenshot(filepath)#保存截图
          logging.info("截图成功，图片路径是：{0}".format(filepath))


      def switch_to_frame(self,locator,model=""):

          self.wait_elevisible(locator)#调用等待方法
          web=self.driver.find_element(locator[0],locator[1])#调用查找元素方法

          try:
            logging.info("切换到iframe")
            self.driver.switch_to.frame(web)#切换到新页面
          except:
            #捕获异常到日志中
            logging.exception("等待元素可见：")
            #截图---保存到的指定的目录
            self._screenshot(model)
#            #抛出异常
            raise

        #上传操作
      def upload(self):
          pass