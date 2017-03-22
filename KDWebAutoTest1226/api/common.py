#coding:utf-8
#!/usr/bin/env python
#*************************************************************************************************
#LogResultDir 判断创建日志、报告存储目录
#Writelog 自定义日志写入
#ComAction webderver等相关操作
#SSHTelnet ssh登陆并获取配置文件的值
#MenuPage 进入各级菜单
#2016-07-28修改
#***************************************************************************************************
import time,os,datetime,linecache,shutil,sys,glob,telnetlib
import paramiko
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from cProfile import Profile
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from driverID import WebID
from api.messages import Getipcmessage
import ConfigParser


cf = ConfigParser.ConfigParser()
cf.read(r'.\Config.ini')
logdir =cf.get("common","log_path")
profiledir =cf.get("common","profiledir")
reload(sys)
sys.setdefaultencoding( "utf-8" )


class Writelog():
    def __init__(self): #存储中文日志是解决编码问题
        reload(sys)
        sys.setdefaultencoding( "utf-8" )
        self.logdir =logdir
    def printlog(self,message):
        now = datetime.datetime.now()
        nowprint=now.strftime('%Y-%m-%d') ##当前时间 年月日 时分秒
        self.logname = r"%s\log-%s.txt" % (self.logdir,nowprint)
        print self.logname
        self.lognamebak = r"%s-bak" % (self.logname)
        self.logfilewrite = open(self.logname, 'a')
        self.size=os.path.getsize(self.logname)
        if self.size>102400:
            os.rename(self.logname,self.lognamebak)
            logfilewrite = open(self.logname1, 'a')
        ISOTIMEFORMAT='%Y-%m-%d %X'   
        print (time.strftime(ISOTIMEFORMAT,time.localtime())+'  :  '+str(message))
        self.logfilewrite.write(time.strftime(ISOTIMEFORMAT,time.localtime())+'  :  '+str(message)+'\n') 
        self.logfilewrite.close()

class ComAction (WebID,Writelog):
    def __init__(self):
        Writelog.__init__(self)
    def wait(self,s=1):    ##定义等待时间，默认1s
        t = time
        t.sleep(1)
        return s
    #********************************************************************************************
    #初始化、打开浏览器
    #********************************************************************************************
    def open_firefox(self):
        self.profiledir = profiledir
        self.profile=webdriver.FirefoxProfile(self.profiledir)
        self.driver=webdriver.Firefox(self.profile)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.firepid = os.getpid()
        print "Firefox PID:",self.firepid
    def open_url(self,ip):   ##打开登录地址
        self.base_url = 'http://'+ip
        self.open_firefox()
        self.driver.get(self.base_url)
        self.wait()
    
    #********************************************************************************************
    #定义各类公共操作
    #*******************************************************************************************
    def switch_frame(self,frame):    ##判断、进入frame
        flag=True
        n=0        
        while flag==True and n<3: 
            try:
                if frame == "contentframe":
                    self.driver.switch_to.frame(frame)
                else:
                    self.driver.switch_to_default_content()
                flag=False
            except BaseException as msg:
                print msg
                self.printlog("switch_frame faileApior"+n+"times")                
                self.driver.refresh()
                n=n+1
    def find_element(self,*loc):    ##基于By,id/name/class/xpath等对象定位,找不到对象时尝试三次
        flag = True
        n =0
        while flag == True and n<3:
            try:
                return self.driver.find_element(*loc)
                flag = False
            except BaseException as msg:
                pass
                print msg
                #lib.write_log.logwrite(*loc+"not found by id" +strApi)
                self.driver.refresh()
                self.switch_to_frame('contentframe')
                n = n+1
        if n ==3:
            self.printlog(*loc+"not found by id")   
    def clickID(self,*loc):    ##基于ID的对象点击操作
        try:
            self.logtext(*loc)
            return self.driver.find_element(*loc).click()
        except BaseException as msg:
            msg = str(msg)
            print msg
            self.printlog(msg)
        
    def logtext(self,*loc):                                 ##存储对象text值
        self.label = self.driver.find_element(*loc).text
        #print self.label
        self.printlog(self.label)
    def type_value(self,text,*loc):                                     ##对象赋值
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(text)
        self.wait()
    def type_casevalue(self,text,*loc):                                     ##对象赋值
        self.find_element(*loc).send_keys(Keys.CONTROL,'a')
        self.wait()
        self.find_element(*loc).send_keys(text,Keys.ENTER)
        self.wait()
    def select_casevalue(self,value,*loc):                                     ##对象赋值
        self.wait()
        self.select=Select(self.find_element(*loc))
        self.select.select_by_value(value)
        self.wait()
        self.find_element(*loc).send_keys(Keys.ENTER)
        self.wait()
    def confim_alert(self):                                  ##处理弹出窗口
        try:
            self.wait()
            alert=self.driver.switch_to_alert()
            alert.accept()()            
            self.wait()
        except BaseException as msg:
            print msg
            #Writelog.printlog("confim_alert not found")
    def closeApirefox(self):                       ##强制杀死Firefox浏览器
        try:
            command='taskkill /F /IM firefox.exe'
            os.system(command)
        except BaseException as msg:
            print msg
            self.printlog("browser close failed")
    ####################进入个页面菜单###########Api####################
    #
    #################################################################
    def enter_menu(self,*loc): 
        try:
            self.driver.switch_to_default_content()    ##跳出frame
        except BaseException as msg:
            pass
            print msg

        if not self.find_element(*loc).is_displayed():  ##判断对象元素是否显示，不显示则点击
                self.clickID(*loc)
        self.clickID(*loc)
        self.wait()
        try:
            self.driver.switch_to_frame('contentframe') ##检查这个元素是否在一个frame中，放在对象操作之前
        except BaseException as msg:
            pass
            print msg
    def enter_page(self,*loc):
        try:
            if not self.find_element(*loc).is_displayed():  ##判断对象元素是否显示，不显示则点击
                self.clickID(*loc)
            self.clickID(*loc)
        except:
            pass

    ####################################################################
    #         登陆
    ######################################################################
    def type_user_passwd(self,username,password,*loc):  ##定位用户名/密码框并赋予用户名/密码value
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
    def checkbox(self):
        checkboxs = self.driver.find_element_by_css_selector('input[type=checkbox]')
        for checkbox in checkboxs:
            checkbox.click()
        time.sleep(5)

class SSHTelnet():
    def sshipc(self,cmd):
            m=Getipcmessage()
            ip =m.getcfgip()
            username = m.getcfgusername()
            passwd = m.getcfgpassword()
            #print ip,username,passwd
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip,22,username,passwd,timeout=5)
            for m in cmd:
                stdin, stdout, stderr = ssh.exec_command(m)
                out = stdout.readlines()
                x=type(out)
                #print 'sshout:'
                print x
                for o in out:
                    ver = o.strip('\n')
                    print ver
            return ver
            ssh.close()
    def getvalue(self,cmd):   ##读取配置文件--->日夜模式值
            val=self.sshipc(cmd)
            val = str(val)
            print "ssh连接设备，获取配置文件值:"+val
            return val
        
    def telnet_ipc(self,host,username,password,logpath):
        tn = telnetlib.Telnet(host,port=17230,timeout=10)
        #tn.set_debuglevel(2)
        time.sleep(1)
        try:
            tn.open(host,port=17230)
        except:
            print "Cannot open host"
            return
        tn.read_until("Username:",timeout=2)
        print username
        tn.write(username+ "\r\n")
        time.sleep(1)
        tn.read_until("Password:")
        print password
        tn.write(password+ "\r\n")
        time.sleep(2)
        tn.write("ipclog 3"+"\r\n")
        
        fileHandle=open(logpath,'a')
        while 1>0:
            klog=tn.read_very_eager()  ##  
            #写入日志
            fileHandle.write(klog)
            fileHandle.flush()   #没有关系
        fileHandle.close()    
                   
class MenuPage(ComAction):
    ################################################################
    #进入各个主页面菜单（实时浏览、录像回放、图片管理、配置）
    #################################################################
    def loginipc(self):
        cfg = Getipcmessage()
        ip = cfg.getcfgip()
        username = cfg.getcfgusername()
        password = cfg.getcfgpassword()
        self.loginIPC(ip,username,password)
    def MenuViewer(self):   ##进入实时浏览页面
        self.enter_menu(*self.MenuViewer_loc)
    def MenuPlayback(self):   ##进入录像回放页面
        self.enter_menu(*self.MenuPlayback_loc)
    def MenuPic(self,*loc):    ##进入图片管理
        self.enter_menu(*self.MenuPic_loc)
    def MenuConfig(self,*loc):    ##进入配置
        self.enter_menu(*self.MenuConfig_loc)
        if self.MenuConfig_loc == "MenuConfig":
            if not self.find_element(*self.MLocalConfig_loc).is_displayed():  ##判断”本地配置“元素是否显示
                self.find_element(*self.MLocalConfig_loc).click()
            self.clickID(*self.aMLocalConfig_loc)   
            self.find_element(*self.MLocalConfig_loc).click()
    ################################################################
    #进入配置页面各个主菜单（本地配置、快速设置、网络、摄像机、时间、存储、系统配置）
    #################################################################
    def aMLocalConfig(self):
        self.MenuConfig()
        self.enter_page(*self.aMLocalConfig_loc)
    def Mfastset(self):
        self.MenuConfig()
        self.enter_page(*self.Mfastset_loc)
    def aNetwork(self):
        self.MenuConfig()
        self.enter_page(*self.aNetwork_loc)
    def aVideoCamera(self):
        self.MenuConfig()
        self.enter_page(*self.aVideoCamera_loc)
    def aEvent(self):
        self.MenuConfig()
        self.enter_page(*self.aEvent_loc)
    def aStorage(self):
        self.MenuConfig()
        self.enter_page(*self.aStorage_loc)
    def aBaseConfig(self):
        self.MenuConfig()
        self.enter_page(*self.aBaseConfig_loc)
    #*********************************************************************************************
    #进入摄像机二级菜单（图像、OSD、视频、音频）
    #*********************************************************************************************
    def aImagsSettings(self):
        #self.aMLocalConfig()
        self.aVideoCamera()
        self.enter_page(*self.aImagsSettings_loc)
    def aOSD(self):
        self.aVideoCamera()
        self.enter_page(*self.aOSD_loc)
    def aVideo(self):
        self.aVideoCamera()
        self.enter_page(*self.aVideo_loc)
    def aAudio(self):
        self.aVideoCamera()
        self.enter_page(*self.aAudio_loc)     
    #*********************************************************************************************
    #进入系统二级菜单（设备信息、用户安全、时间设置、串口、日志管理、系统维护）
    #*********************************************************************************************
    def aDeviceInformation(self):
        self.aBaseConfig()
        self.enter_page(*self.aDeviceInformation_loc)  
    def aSecurity(self):
        self.aBaseConfig()
        self.enter_page(*self.aSecurity_loc) 
    def aDateTime(self):
        self.aBaseConfig()
        self.enter_page(*self.selfaDateTime_loc) 
    def aSerialPost(self):
        self.aBaseConfig()
        self.enter_page(*self.aSerialPost_loc) 
    def aLog(self):
        self.aBaseConfig()
        self.enter_page(*self.aLog_loc) 
    def aSystemMaintenance(self):
        self.aBaseConfig()
        self.enter_page(*self.aSystemMaintenance_loc) 
        
        

if __name__ == '__main__':   ##进行函数测试
    test = Writelog()
    message = '1111111111111111111111'
    test.printlog(message)
