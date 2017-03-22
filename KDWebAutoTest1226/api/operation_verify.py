#coding:utf-8
#!/usr/bin/env python
##################################################################
#
#
#2016-05-3修改
##################################################################
import time
from api import common
#from common.Writelog import printlog
from menupage import MenuPage
from msilib.schema import CheckBox
from api.common import *
from messages import Getipcmessage


class Loginipc(ComAction):
    def __init__(self):
        lg = ComAction()
        cfg = Getipcmessage()
        ip = cfg.getcfgip()
        username = cfg.getcfgusername()
        password = cfg.getcfgpassword()
        lg.loginIPC(ip,username,password)

class ssh_simplerestore():
    def enablessh(self):
        entermenu =self.aSecurity()
        self.clickID(*self.MSafetyService_loc)
        time.sleep(2)
        self.find_element(*self.IsEnableSSH_loc).click()
        time.sleep(1)
        self.clickID(*self.SaveSafetyService_loc)
    def simplerestore(self):
        entermenu =self.aSystemMaintenance()
        time.sleep(2)
        self.clickID(*self.aSimpleRestore_loc)
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        time.sleep(60)

class operation(MenuPage,SSHTelnet):
    def operation_sendkeys(self,casevalue,case,cmd,*loc):
        list1 = casevalue
        print list1
        for i in list1:
            #print case+'测试值:'+str(i)
            #print type(case)
            #self.aImagsSettings()
            self.printlog(case+'当前测试值:'+i)
            i=str(i)
            x=type(i)
            print x
            self.type_casevalue(i,*loc)
            #self.capture(case, i)
            time.sleep(1)
            r=self.getvalue(cmd)
            s=type(r)
            print s
            if i ==r:
                self.printlog(case+'当前测试值:'+i+'：测试 OK'+'...'+"\r\n")
            else:
                #print case+'测试值:'+i+"本测试用例执行失败"
                self.printlog(case+'测试值:'+i+'：时测试用例执行失败')
            time.sleep(10)
    def operation_select(self,casevalue,case,cmd,*loc):
        list1 = casevalue
        print list1
        for i in list1:
            print case+'测试值:'+str(i)
            #print type(case)
            self.printlog(case+'当前测试值:'+i)
            i=str(i)
            adict={'manual':'0','auto':'1','dc_irismanual':'0','dc_irisauto':'1','p_irismanual':'2','50hz':'0','60hz':'1','auto':'2'
                   ,'1/7.5':'0','1/10':'1','1/15':'2','1/25':'4','1/50':'6','1/100':'8','1/240':'10','1/480':'11','1/960':'12','1/1024':'13','1/8000':'14'
                   ,'1/16000':'15','1/1':'16','1/2':'17','1/150':'18','1/200':'19','1/2000':'20','1/4000':'21','1/30000':'22','auto1':'1','auto2':'2'
                   ,'lock':'3','fluorescentlight':'4','filamentlight':'5','warmlight':'6','natural':'7','open':'1','close':'0','autoblc':'1','regionblc':'3'
                   ,'hlc':'2','wdr':'4','gamma':'1'}
            i1 = adict.get(i)
            x=type(i)
            #print x
            self.select_casevalue(i,*loc)
            #self.capture(case, i)
            time.sleep(1)
            r=self.getvalue(cmd)
            s=type(r)
            #print s

            if i1 ==r:
                self.printlog(case+'当前测试值:'+i+'：测试 OK')
            else:
                #print case+'测试值:'+i+"本测试用例执行失败"
                self.printlog(case+'测试值:'+i+'：时测试用例执行失败')
            time.sleep(10)

    def avideo_sendkeys(self,casevalue,case,cmd,*loc):
        list1 = casevalue
        print list1
        for i in list1:
            #print case+'测试值:'+str(i)
            #print type(case)
            #self.aImagsSettings()
            self.printlog(case+'当前测试值:'+i)
            i=str(i)
            x=type(i)
            #print x
            self.type_casevalue(i,*loc)
            self.clickID(*self.ConfigBtn_loc)
            time.sleep(1)
            r=self.getvalue(cmd)
            s=type(r)
            #print s
            if i ==r:
                self.printlog(case+'当前测试值:'+i+'：测试 OK')
            else:
                #print case+'测试值:'+i+"本测试用例执行失败"
                self.printlog(case+'测试值:'+i+'：时测试用例执行失败')
            time.sleep(5)
    def ovideo_select(self,casevalue,case,cmd,*loc):
        list1 = casevalue
        print list1
        for i in list1:
            print case+'测试值:'+str(i)
            #print type(case)
            self.printlog(case+'当前测试值:'+i)
            i=str(i)
            x=type(i)
            #print x
            self.select_casevalue(i,*loc)
            self.clickID(*self.ConfigBtn_loc)
            time.sleep(1)
            r=self.getvalue(cmd)
            s=type(r)
            #print s
            if i ==r:
                self.printlog(case+'当前测试值:'+i+'：测试 OK')
            else:
                #print case+'测试值:'+i+"本测试用例执行失败"
                self.printlog(case+'测试值:'+i+'：时测试用例执行失败')
            time.sleep(5)
