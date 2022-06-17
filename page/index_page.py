"""
@author:maohui
@time:2022/6/17 11:00
  　　　　　　　 ┏┓    ┏┓+ +
  　　　　　　　┏┛┻━━━━┛┻┓ + +
  　　　　　　　┃        ┃ 　 
  　　　　　　　┃     ━  ┃ ++ + + +
  　　　　　 　████━████ ┃+
  　　　　　　　┃        ┃ +
  　　　　　　　┃   ┻    ┃
  　　　　　　　┃        ┃ + +
  　　　　　　　┗━┓   ┏━━┛
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃ + + + +
  　　　　　　　  ┃   ┃　　　Code is far away from bug with the animal protecting
  　　　　　　　  ┃   ┃+ 　　　　神兽保佑,代码无bug
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃　　+
  　　　　　　　  ┃   ┗━━━━━━━┓ + +     
  　　　　　　　  ┃           ┣┓
  　　　　　　　  ┃           ┏┛
  　　　　　　　  ┗┓┓┏━━━━━┳┓┏┛ + + + +
  　　　　　　　   ┃┫┫     ┃┫┫
  　　　　　　　   ┗┻┛     ┗┻┛+ + + +
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class IndexPage():
    #元素定位
    def __init__(self,driver):
        self.indexadmin_loc=(By.XPATH,"//*[@id='wrapper']/div[1]/div/div[2]/ul/li[3]/a/div/span")
        self.driver=driver
        # self.driver=webdriver.Chrome()
        self.wait=WebDriverWait(self.driver,20)
    #页面操作
    def indexadmin_click(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.indexadmin_loc))
            self.driver.find_element(*self.indexadmin_loc).click()
        except Exception as e:
            self.driver.get_screenshot_as_file("../log_pic/点击首页管理错误.png")

# if __name__=="__main__":
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://well-healthcare.com/EN/CMS/Login.aspx")
