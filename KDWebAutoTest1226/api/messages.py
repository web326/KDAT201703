#coding:utf-8
#!/usr/bin/env python
##################################################################
#定义获取IPC设备信息的函数
#1.通过ConfigParser获取、配置IPCconfig.ini文件中IP、username、password等信息；
#2.通过xlrd读取excel中设备IP、username、password等信息；
#若使用图像化界面使用1方案，方便界面上修改保存信息
#2016-07-20 吴卫彬修改
##################################################################
import xlrd,os,ConfigParser
from paramiko.config import SSH_PORT

class Getipcmessage():
    def __init__(self):  ##获取配置文件路径及打开获取ini文件sections       
        self.dirpwd = os.path.abspath('.') 
        self.cfgname = r'%s\Config.ini' %self.dirpwd  
        self.cf = ConfigParser.ConfigParser() 
        self.cf.read(self.cfgname)
        secs = self.cf.sections()
        opts = self.cf.options("common") 
    def getcfgip(self):     ##获取配置文件中信息  
        self.ip = self.cf.get("common","host")
        return self.ip
    def getcfgusername(self):     ##获取配置文件中信息  
        self.username = self.cf.get("common","username")
        return self.username
    def getcfgpassword(self):     ##获取配置文件中信息  
        self.password = self.cf.get("common","password")
        return self.password
    def getcfgsshport(self):     ##获取配置文件中信息  
        self.SSH_port = self.cf.get("common","SSH_port")
        return self.SSH_port
    def getcfgtelnetport(self):     ##获取配置文件中信息  
        self.telnet_port = self.cf.get("common","telnet_port")      
        return self.telnet_port

        
    def setcfgip(self,value):   ##设置IP信息到配置文件
        self.cf.set("common", "host", value)
        self.cf.write(open(self.cfgname,"w"))
        
    def setcfgusername(self,value):   ##设置username信息到配置文件
        self.cf.set("common", "username", value)
        self.cf.write(open(self.cfgname,"w"))
        
    def setcfguspassword(self,value):   ##设置password信息到配置文件
        self.cf.set("common", "password", value)
        self.cf.write(open(self.cfgname,"w"))
        
    def setcfgusshport(self,value):   ##设置ssh_port信息到配置文件
        self.cf.set("common", "ssh_port", value)
        self.cf.write(open(self.cfgname,"w"))
        
    def setcfgutelnetport(self,value):   ##设置telnet_port信息到配置文件
        self.cf.set("common", "telnet_port", value)
        self.cf.write(open(self.cfgname,"w"))
        
        
class Getexcelvalue():
    def getexcelmessage(self):
        dirpwd = os.path.abspath('..') 
        excelname = r'%s\Config\IPC_v7_message.xlsx' %dirpwd
        print "设备信息存储路径"+excelname
        opensheet = xlrd.open_workbook(excelname)
        ip_list = []
        user_list = []
        password_list = []
        sshport_list = []
        telnetport_list = []
        
        try:
            sheet = opensheet.sheet_by_name("message")
        except BaseException as msg:
            print ("no sheet in %s named message") %excelname
            print msg
            
        nrows = sheet.nrows  #获取行数
        ncols = sheet.ncols  #获取列数
        
        for i in range(2,nrows): #行 循环
            self.ip = sheet.cell_value(i,1)
            ip_list.append(self.ip)
            self.username = sheet.cell_value(i,2)
            user_list.append(self.username)
            self.password = sheet.cell_value(i,3)
            password_list.append(self.password)
            self.SSH_port = sheet.cell_value(i,4)
            sshport_list.append( self.SSH_port)
            self.telnet_port = sheet.cell_value(i,5)
            telnetport_list.append(self.telnet_port)
            print self.ip,self.username,self.password, self.SSH_port,self.telnet_port
if __name__ == '__main__':   ##进行函数测试
    get = Getipcmessage()
    #get.setcfgsshport(23)
    #get.setcfgip('192.168.25.71')
    print get.getcfgip()