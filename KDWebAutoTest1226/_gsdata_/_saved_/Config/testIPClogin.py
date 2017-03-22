#coding:utf-8
###==================
##Created on 2016年10月20日
##@author: wuweibin
###==================
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from cProfile import Profile
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
ip = '192.168.252.132'
username = 'admin'
password = 'admin123'

class  IPClogin():
    def open_firefox(self):
        self.profileDir="C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/dsobmwpl.default-1466480030910"  ##需要根据自己路径获取
        #self.profileDir="C:/Users/admin/AppData/Roaming/Mozilla/Firefox/Profiles/d68dofkn.default"
        self.profile=webdriver.FirefoxProfile(self.profileDir)
        self.driver=webdriver.Firefox(self.profile)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def open_url(self,ip):   ##打开登录地址
        self.base_url = 'http://'+ip
        self.open_firefox()
        self.driver.get(self.base_url)
        self.wait()
    def type_value(self,text,*loc):                                     ##对象赋值
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(text)
        self.wait()
    def type_user_passwd(self,username,password,*_loc):  ##定位用户名/密码框并赋予用户名/密码value
        print username,password
        self.type_value(username,*self.username_loc)
        self.type_value(password,*self.password_loc)
    def clickLogin(self):    ##点击登录按钮
        self.wait()
        self.clickID(*self.login_loc)
    def loginIPC(self,ip,username,password):   ##登录IPC函数
        self.open_url(ip)
        self.type_user_passwd(username, password)
        self.clickLogin()
        self.confim_alert()
        self.now_url=self.driver.current_url
        print self.now_url
        #self.printlog(self.now_url)

if __name__ == '__main__':
    IPC = IPClogin()
    IPC.loginIPC(ip, username, password)