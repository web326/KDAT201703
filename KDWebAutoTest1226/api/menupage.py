#coding:utf-8
#!/usr/bin/env python
##################################################################
#
#
#2016-05-3修改
##################################################################
from api.common import *


class MenuPage(ComAction):
    ################################################################
    #进入各个主页面菜单（实时浏览、录像回放、图片管理、配置）
    #################################################################
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
    username = 'admin'
    password = 'admin123'
    case = 'test'
    value = '250250'
    ipc = MenuPage()
    ipc.loginIPC(ip, username, password)
    ipc.aImagsSettings()