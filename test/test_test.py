"""
@author:maohui
@time:2022/6/16 16:04
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

import allure
import pytest
# from selenium import webdriver
# from page.login_page import LoginPage


@pytest.fixture()
def init():
    print('init.............')
    return 1


name_data = ['admin', 'test']


@pytest.mark.parametrize('name', name_data)
def test001(name):
    """正常和错误用户名登录"""
    print(name)
    # """正常和错误用户名登录"""
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get("http://well-healthcare.com/EN/CMS/Login.aspx")
    # loginPage = LoginPage(driver)
    # loginPage.name_input(name)
    # time.sleep(2)


# login_data=[('admin','123456'),('test','123')]
# @pytest.mark.parametrize('name,pwd',login_data)
# def test002(name,pwd):
#     """不同账号密码登录"""
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://well-healthcare.com/EN/CMS/Login.aspx")
#     loginPage = LoginPage(driver)
#     loginPage.name_input(name)
#     loginPage.pwd_input(pwd)
#     time.sleep(2)
#
# login_dic=({'admin':123456,
#             'test':123456},
#            {'age':3,
#             "email":"123@126.com"}
# )
# @pytest.mark.parametrize('dic',login_dic)
# def test002(dic):
#     print(dic)

# if __name__ == "__main__":
#     pytest.main(['test_test.py', 'sv'])
# pytest --alluredir ./report test08.py
# allure serve ./report 启动allure 查看报告