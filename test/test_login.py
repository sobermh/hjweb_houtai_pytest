"""
@author:maohui
@time:2022/6/17 9:16
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
import time

import pytest
from selenium import webdriver
from page.login_page import LoginPage


class TestLogin(object):

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://well-healthcare.com/EN/CMS/Login.aspx")
        self.driver.maximize_window()
        self.LoginPage = LoginPage(self.driver)

    name_data = ['admin']

    @pytest.mark.dependency(name='admin_login')
    @pytest.mark.parametrize('name', name_data)
    def test001(self,name):
        """正确用户名密码登录成功"""
        self.LoginPage.name_input(name)
        self.LoginPage.pwd_input('123456')
        self.LoginPage.authcode_input()
        time.sleep(2)

    login_data = [('admin', '123456'), ('test', '123')]

    @pytest.mark.parametrize('name,pwd', login_data)
    def test002(self, name, pwd):
        """不同账号密码登录"""
        self.LoginPage.name_input(name)
        self.LoginPage.pwd_input(pwd)
        self.LoginPage.authcode_input()
        time.sleep(2)

    def teardown(self):
        self.driver.quit()
