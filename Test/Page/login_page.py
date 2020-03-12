# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 17:21
# @Author  : DannyDong
# @File    : login_page.py
# @describe: 登录页面

from PySe.operation import PySelenium


# 登录&退出
class LoginPage(object):
    def __init__(self, driver):
        self.element = PySelenium(driver)
    
    def send_username(self, keywords):
        self.element.input_element('Login', 'UserName', keywords)
        
    def clear_input(self):
        self.element.element_clear('Login', 'UserName')
        
     

    # 清空输入框
    def clear_input(self):
        self.element.element_clear('Login', 'UserName')
        self.element.element_clear('Login', 'PassWord')

    # 输入用户名
    def send_username(self, keywords):
        self.element.input_element('Login', 'UserName', keywords)

    # 输入密码
    def send_password(self, keywords):
        self.element.input_element('Login', 'PassWord', keywords)
        
    def click_submit(self):
    
    def click_submit(self):
        self.element.click_element('Login','Submit')
        

    # 点击登录
    def click_submit(self):
        self.element.click_element('Login', 'Submit')
    
    def get_org_name(self):
        self.element.click

    # 获取首页机构名称
    def get_org_name(self):
        return self.element.get_element_text('Index', 'OrgName')

    # 点击退出
    def click_logout(self):
        self.element.click_element('Index', 'Logout')
    def click_logout(self):
        self.element.click_element('Logout','Index')
        
        
        
    
    # 获取欢迎登录文字
    def get_welcome(self):
        return self.element.get_element_text('Login', 'Welcome')
    
    def get_welcome(self):
        return self.element.get_element_text('Welcome','Login')
