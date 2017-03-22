#coding=utf-8
##IPCweb执行日夜切换1000次
import unittest,time    #导入单元测试unittest和时间time模块
from selenium import webdriver   #从selenium中导入webdriver
from selenium.webdriver.support.select import Select    #导入Select处理下来菜单选择框

host = '192.168.251.126'
username = 'admin'
password = 'admin123'
tester='吴卫彬'
ISOTIMEFORMAT='%Y-%m-%d %X'   #时间显示格式
class Test1():
    def test1(self):
        print "test 111   test1"
        
class action():     #公共操作类
    def login(self,username,password):      #登陆函数
        time.sleep(1)    #等待1秒
        self.driver.find_element_by_id("username").send_keys(username)      #输入用户名
        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys(password)      #输入密码
        time.sleep(1)
        self.driver.find_element_by_id("b_Login").click()       #点击登陆
        time.sleep(1)
    def Day_night(self):        #进入日夜切换菜单
        time.sleep(0.5)
        self.driver.find_element_by_id("MenuConfig").click()        #进入配置页面
        time.sleep(0.5)
        self.driver.switch_to_frame('contentframe')         #切换contentframe
        time.sleep(0.5)
        self.driver.find_element_by_id("aVideoCamera").click()      #进入摄像机菜单
        time.sleep(0.5)
        self.driver.find_element_by_id("aImagsSettings").click()      #进入图像菜单
        time.sleep(0.5)
        self.driver.find_element_by_id("ircutfilterh5").click()             #打开日夜切换
        time.sleep(0.5)
    def Day_night_change(self):         #日夜切换操作函数
        ##夜：night  白天：day 自动增益：auto_gain  自动光敏：auto_photot.sleep(0.5)
        self.driver.find_element_by_id("IrcutfilterType").click()           #打开日夜切换下来菜单
        self.select=Select(self.driver.find_element_by_id('IrcutfilterType'))       #定位选择框
        self.select.select_by_value('night')        #输入切换数值
        self.driver.find_element_by_id("IrcutfilterType").click()       #关闭日夜切换下来菜单
        time.sleep(60)                      #日夜切换间隔 10秒
        self.driver.find_element_by_id("IrcutfilterType").click()
        self.select=Select(self.driver.find_element_by_id('IrcutfilterType'))
        self.select.select_by_value('day')  
        self.driver.find_element_by_id("IrcutfilterType").click()
        time.sleep(60)

class DayNightchange(unittest.TestCase,action):     #日夜切换，继承父类unittest.TestCase,action
    def setUp(self):    #日夜切换测试，初始化操作
        print '测试人员：'+tester+'  设备：'+host+'  测试开始：'+time.strftime( ISOTIMEFORMAT, time.localtime() )      #显示开始测试时间
        self.profileDir="C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/dsobmwpl.default-1466480030910"   
        self.profile=webdriver.FirefoxProfile(self.profileDir)    
        self.driver=webdriver.Firefox(self.profile)  #初始化浏览器，使启动的浏览器可以加载已配置的信息
        self.driver.maximize_window()      #最大化浏览器
        self.driver.implicitly_wait(30)    #隐形等待浏览器启动时间30秒
        self.driver.get('http://'+host)         #输入IP地址
        self.login(username,password)       #调用login函数登陆IPC
        self.Day_night()        #调用Day_night()，进入到日夜切换菜单
    def tearDown(self):   #测试结束，环境恢复
        print '测试结束：'+time.strftime( ISOTIMEFORMAT, time.localtime() )
        self.driver.quit()
    def test_01(self):      #测试用例
        n=0     #设置长拷的次数
        while (n<1000): 
            n=n+1
            self.Day_night_change()     #执行日夜切换
            print '执行第：'+str(n)+' 次   '+time.strftime( ISOTIMEFORMAT, time.localtime() )   #打印执行的测试

if __name__ == "__main__":      #main函数
    suite = unittest.TestSuite()    #创建测试套件
    suite.addTest(DayNightchange('test_01'))  #将test_01添加到测试套件中
    #运行测试套件
    runner = unittest.TextTestRunner()      #
    runner.run(suite)       #
    
