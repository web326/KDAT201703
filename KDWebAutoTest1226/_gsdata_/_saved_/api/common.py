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


class LogResultDir():
    def nowdir(self):
        logsdir = os.path.abspath('.') 
        return logsdir
    def logsdir(self):
        logsdir = os.path.abspath('..\Logs')       ##获取result目录绝对路径
        ISOTIMEFORMAT='%Y-%m-%d'  
        logname = time.strftime(ISOTIMEFORMAT,time.localtime()) 
        logdirname = logsdir+'\\'+logname
        if os.path.exists(logdirname):
            pass
        else:
            try:
                os.makedirs(logdirname)
            except BaseException as msg:
                pass
                print msg
        return logdirname
    def resultdir(self):
        resultpath = os.path.abspath('..\TestResult')       ##获取result目录绝对路径
        ISOTIMEFORMAT='%Y-%m-%d'  
        resultname = time.strftime(ISOTIMEFORMAT,time.localtime()) 
        resultdirname = resultpath+'\\'+resultname
        if os.path.exists(resultdirname):
            pass
        else:
            try:
                os.makedirs(resultdirname)
            except BaseException as msg:
                pass
                print msg
        return resultdirname
    def picdir(self):
        picdirname = self.resultdir()
        picpath = picdirname+'\\'+'pic'            
        if os.path.exists(picpath):
            pass
        else:
            try:
                os.makedirs(picpath)
            except BaseException as msg:
                pass
                print msg
        #print picpath
        return picpath

class Writelog(LogResultDir):
    reload(sys)
    sys.setdefaultencoding( "utf-8" ) #存储中文日志是解决编码问题
    
    def printlog(self,message):
        now1 = datetime.datetime.now()
        nowprint1=now1.strftime('%Y-%m-%d') ##当前时间 年月日 时分秒
        filedir=self.logsdir()
        logname1 = r"%s\log-%s.txt" % (filedir,nowprint1)
        lognamebak = r"%s-bak" % (logname1)
        if os.path.exists(logname1):
            pass
        else:
            try:
                logfilewrite = open(logname1, 'a')
            except BaseException as msg:
                print '文件已存在'+str(msg)
        size=os.path.getsize(logname1)
        if size>102400:
            os.rename(logname1,lognamebak)
    
        logfilewrite = open(logname1, 'a')
        ISOTIMEFORMAT='%Y-%m-%d %X'   
        print (time.strftime(ISOTIMEFORMAT,time.localtime())+'  :  '+str(message))
        logfilewrite.write(time.strftime(ISOTIMEFORMAT,time.localtime())+'  :  '+str(message)+'\n') 
        logfilewrite.close()

class ComAction (WebID,Writelog,LogResultDir):
    def wait(self,s=1):    ##定义等待时间，默认1s
        t = time
        t.sleep(1)
        return s
    #********************************************************************************************
    #初始化、打开浏览器
    #********************************************************************************************
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
            
    #*******************************************************************************************
    #浏览器抓拍+web前段抓拍及图像命名移动到log目录下
    #
    #********************************************************************************************
    def browser_screenshot(self,filename=datetime.datetime.now().strftime("%Y%m%d.%H%M%S.%f")[:-3]):
        ##浏览器窗口截图，默认以时间命名
        self.filedir = LogResultDir.resultlogdir.pictdir()
        print self.filedir,filename
        self.driver.savApicreenshot(self.filedir+'\\'+filename+'.png')
    def picpath(self):  ##获取图片默认路径win7
        self.picpathfile = linecache.getline(r'C:\Users\Public\Documents\IPCWeb\ipcweb.ini',13)   ##需要根据自己的路径调整
        self.filedir = self.picpathfile
        self.localpicpath = self.filedir[13:-1]
        print self.localpicpath
        return self.localpicpath
    def movefile(self,case,value):      ##将图片抓拍路径下最新图片更改名称移动到log/*pic目录
        srcpath = self.picpath()     ##获取图片本地存储路径
        newfiledir = LogResultDir.resultlogdir.picdir()
        print "newfiledir:"+newfiledir
        r = LogResultDir.resultlogdir.nowdir()
        print "r" +r
        os.chdir(srcpath)      ##切换到图片存储路径
        files = os.listdir(".")    ##遍历目录中图片信息
        newfile = [files[-1]]
        print srcpath,newfile
        for filename in newfile:
            li = os.path.splitext(filename)   ##分离文件名与扩展名
            print li
            if li[1] == ".jpg":
                value=str(value)
                newname = datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'-'+case+'-'+value+li[1]   ##拼接图片新名称
                #print newname  
                #print type(newname)
                #print chardet.detect(newname)  ##查看当前编码格式
                newname = newname.decode("utf-8", "ignore").encode("gbk", "ignore")  ##将utf-8编码格式修改为gbk编码格式，解决文件名中文显示乱码问题
                #print chardet.detect(newname)
                self.wait()
                try:
                    os.rename(filename,newname)
                except BaseException as msg:
                    print msg
                srcfilename = self.picpath()+'\\'+newname  ##拼接更改更改名称后图片完整路径
                srcfilename = srcfilename.decode("gbk", "ignore").encode("utf-8", "ignore")
                print "srcfilename:"+srcfilename
                os.chdir(LogResultDir.resultlogdir.nowdir())
                self.wait()
                try:
                    shutil.move(srcfilename,newfiledir)
                except BaseException as msg:
                    print msg
    def capture(self,case,value):  ##实时浏览抓拍图Api
        self.value=value
        self.case=case
        self.MenuViewer()
        self.wait(2)
        flag = False
        n =0
        while flag == False and n<3:
            try:
                self.driver.find_element_by_id('capture').click()
                
                flag = True
            except BaseException as msg:
                print msg
                self.printlog("not found capture" +str(n))
                self.driver.refresh()
                self.switch_to_frame('contentframe')
                n = n+1
        if n ==3:
            self.printlog("not found capture")      
        self.wait()
        self.movefile(case,value)
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
        #tn.read_until("bin->",timeout=2)
        tn.write("ipclog 3"+"\r\n")
        
        fileHandle=open(logpath,'a')
        while 1>0:
            #tn.read_some()
            #time.sleep(2)
     
            klog=tn.read_very_eager()  ##
            #klog=tn.read_very_lazy()
            #print klog 
    
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
    ip = '192.168.25.71'
    username='admin'
    password = 'admin123'
    m = MenuPage()
    m.loginipc()
    entermenu =m.MenuPic()
    cmd = ["cat /usr/config/ipccfg.conf|awk -F DayNightMode '{print $5}'|awk -F , '{print $1"" }'|awk -F : '{print $2}'"]
    ssh = SSHTelnet()
    ssh.getvalue(cmd)

