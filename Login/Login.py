#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '
#==========================
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

AutoRunPath = "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

def SetEnvironment():
    ChromeDriver = "chromedriver.exe"
    print("Please DOWNLOAD chromedriver.exe compare to your Chrome web explorer.")
    os.environ["webdriver.chrome.driver"] = ChromeDriver
    return ChromeDriver

def GetUserAccount():
    Account = {'UserName':'Null', 'PassWord':'Null'}
    with open('user.config', 'r') as config:
        Account['UserName'] = config.readline().rstrip('\n')
        Account['PassWord'] = config.readline().rstrip('\n')
    #print("DEBUG:Username:{},Password:{}".format(Account['UserName'],Account['PassWord']))
    config.close()
    return Account

def Login():
    Ngw = webdriver.Chrome(SetEnvironment())
    Ngw.get("http://ngw.bupt.edu.cn/index")
    Account = GetUserAccount()

    InputUser = Ngw.find_element_by_name("user")
    InputUser.send_keys(Account['UserName'])
    InputPassword = Ngw.find_element_by_name("pass")
    InputPassword.send_keys(Account['PassWord'])
    S1 = Select(Ngw.find_element_by_name("line")).select_by_visible_text("中国联通")

    Btn_Login = Ngw.find_element_by_class_name("el-button--primary")
    Btn_Login.click()

    Ngw.close()



def main():
    Login()


#==========================
if __name__ == '__main__':
    main()