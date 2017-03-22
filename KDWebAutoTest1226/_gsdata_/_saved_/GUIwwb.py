#\usr\bim\python
#coding=utf-8

from Tkinter import *
import Tkinter as tk
from tkFont import Font
from ttk import *
from ctypes import *
from tkMessageBox import *
import time,sys,os,logging,ConfigParser,threading,runstart,ctypes
from runstart import Run_Test 
from api import getcasevalue
from runtest import test_aImagsSettings
psapi = windll.psapi
kernel = windll.kernel32
################接口类部分#####################
class API():
    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(r'Config.ini')
        self.host=StringVar()           #定义变量类型
        self.username=StringVar()
        self.password=StringVar()
        self.log_path=StringVar()
        self.profiledir=StringVar()
        self.check_out = StringVar()
        self.getvalue = StringVar()
        self.v=IntVar()          #给选择哪个功能使用
        self.mv = StringVar()
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.v3 = IntVar()
        self.v4 = IntVar()
        self.v5 = IntVar()
        self.v6 = IntVar()
        self.v7 = IntVar()
        self.pidlist =[]
        self.host.set(self.cf.get("common","host"))          #获取相应的变量
        self.username.set(self.cf.get("common","username"))
        self.password.set(self.cf.get("common","password"))
        self.log_path.set(self.cf.get("common","log_path"))
        self.profiledir.set(self.cf.get("common","profiledir"))
        self.getvalue.set(getcasevalue.light_list)
        self.cf.set("fun","choice_v1",1)    #初始化配置文件初始数值【fun】
        self.cf.set("fun","choice_v2",2)
        self.cf.set("fun","choice_v3",3)
        self.cf.set("fun","choice_v4",0)
        self.cf.set("fun","choice_v5",0)
        self.cf.set("fun","choice_v6",0)
        self.cf.set("fun","choice_v7",0)
        self.cf.write(open(r'Config.ini', "w"))
        if os.path.exists(self.cf.get("common","log_path")):           #根据config.ini文件的log路径判断、创建日志目录
            pass
        else:
            try:
                os.makedirs(self.cf.get("common","log_path"))
            except BaseException as msg:
                pass
                print msg

    def cfsave(self):               #定义保存按钮点击后写入保存配置信息函数
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(r'Config.ini')
        self.cf.set("common","host",self.host.get())
        self.cf.set("common","username",self.username.get())
        self.cf.set("common","password",self.password.get())
        self.cf.set("common","log_path",self.log_path.get())
        self.cf.set("common","profiledir",self.profiledir.get())
        self.cf.write(open("Config.ini", "w"))
    def callbutton(self):      ##定义button按钮调用函数，没有意义。。。。。
        print self.mv.get()
        print "干什么？？？"
    def all_value(self):   ##定义图像全选按钮，待研究。。。。。？？？？
        print "全选按钮，未实现"
    def notall_value(self):   ##定义图像取消全选按钮，待研究。。。。。？？？？
        print "取消全选，未实现"
    def choice_v1(self):    ##定义第一个复选框调用函数，例如：亮度调节，取消勾选设置choice_v1为0，选中设置为1
        self.value=self.v1.get()    
        print self.value
        self.cf.set("fun","choice_v1",str(self.value))
        self.cf.write(open(r'Config.ini', "w"))
        #self.choice_value = self.cf.get("gui","choice_v1")   #显示选中的值，但是复现框有问题，不知道如何显示，待研究。。。。。？？？
    def choice_v2(self):
        self.value=self.v2.get()
        print self.value
        self.cf.set("fun","choice_v2",str(self.value))
        self.cf.write(open(r'Config.ini', "w"))
    def choice_v3(self):
        self.value=self.v3.get()
        print self.value
        self.cf.set("fun","choice_v3",str(self.value))
        self.cf.write(open(r'Config.ini', "w"))
    def choice_v4(self):
        self.value=self.v4.get()
        print self.value
        self.cf.set("fun","choice_v4",str(self.value))
        self.cf.write(open(r'Config.ini', "w"))
    def choice_v5(self):
        self.value=self.v5.get()
        print self.value
        self.cf.set("fun","choice_v5",str(self.value))
        self.cf.write(open(r'Config.ini', "w"))
    def choice_v6(self):
        self.value=self.v6.get()
        print self.value
        self.cf.set("fun","choice_v6",str(self.value))
        self.cf.write(open(r'Config.ini', "w"))
    def choice_v7(self):
        self.value=self.v7.get()
        print self.value
        self.cf.set("fun","choice_v7",str(self.value))
        self.cf.write(open(r'Config.ini', "w"))

    #######定义开始按钮的后的一系列操作########################

    def  check_ping(self):               #定义ping IPC的IP，判断配置网络是否通
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(r'Config.ini')
        self.host = self.cf.get("common","host")
        self.ping_return=os.system('ping -n 1 -w 1 %s'%self.host) #每个ip ping1次，等待时间为1s 
        if self.ping_return: 
            self.ping_out= str('Ping %s is fail'%self.host) #需要考虑如何显示在GUI上面
            self.check_out.set(self.ping_out)
            return
        else: 
            self.ping_out=str('Ping %s is OK，网络无异常，开始测试'%self.host) #需要考虑如何显示在GUI上面
            self.check_out.set(self.ping_out)
        time.sleep(1)
        
    def check_log(self):           ##定义显示显示窗口显示信息
        ISOTIMEFORMAT='%Y-%m-%d %X'   
        self.time_out=(time.strftime(ISOTIMEFORMAT,time.localtime()))
        self.check_out.set(self.time_out)
        print self.time_out
    def ipc_func(self):   ##创建功能运行的线程函数
        self.funrun = Run_Test()
        t=threading.Thread(target=self.funrun.fun_dict)
        t.setDaemon(True)
        t.start()

################GUI界面部分##########################################
#GUI显示相关，实现界面生成功能
######################################################################
class GUI(Frame,API):
    def __init__(self, master=None):   
        Frame.__init__(self, master)     #从Frame派生一个Application类
        self.master.title('KIPC功能自动化测试')   ##TK窗口的title显示
        self.master.geometry('800x600')   ##TK窗口的大小
        API.__init__(self)        #
        self.createWidgets()               ##创建容器
        self.pid = os.getpid()           ##获取当前界面运行PID
    def test_begin(self):         ##界面上开始按钮调用函数，使用多线程可以使界面不卡死，实现：运行时可操作按钮禁用，进行检查，功能运行
        self.check_out.set("已点击开始按钮，功能自动化开始")
        threads = []
        t1 =threading.Thread(target=self.start_disable)
        threads.append(t1)
        print t1.isAlive()
        t2 = threading.Thread(target=self.check_ping)
        threads.append(t2)
        t3 = threading.Thread(target=self.ipc_func)
        threads.append(t3)
        for t in threads:
            t.setDaemon(True)
            t.start()

    def enumProcesses(self):
            arr = c_ulong * 256
            lpidProcess= arr()
            cb = sizeof(lpidProcess)
            cbNeeded = c_ulong()
            hModule = c_ulong()
            count = c_ulong()
            modname = c_buffer(30)
            PROCESS_QUERY_INFORMATION = 0x0400
            PROCESS_VM_READ = 0x0010
            psapi.EnumProcesses(byref(lpidProcess),cb,byref(cbNeeded))
            nReturned = cbNeeded.value/sizeof(c_ulong())
            pidProcess = [i for i in lpidProcess][:nReturned]
            pidd = {}
            firefoxpid = {}
            for pid in pidProcess:
                #Get handle to the process based on PID
                hProcess = kernel.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ,False, pid)
                if hProcess:
                    psapi.EnumProcessModules(hProcess, byref(hModule), sizeof(hModule), byref(count))
                    psapi.GetModuleBaseNameA(hProcess, hModule.value, modname, sizeof(modname))
                    name= "".join([ i for i in modname if i != '\x00'])
                    pidd[pid]=name
                    for i in range(modname._length_):
                        modname[i]='\x00'
                    kernel.CloseHandle(hProcess)
            for (key, value) in pidd.items():
                if value.startswith(u'firefox.exe'):
                    firefoxpid[key] = value
            for tid in firefoxpid.keys():
                self.pidlist.append(int(tid))
            self.pidlist.sort()
            #print self.pidlist
            return self.pidlist
    def set_stop(self):   ##定义停止功能运行函数。。。。。。。。现在还有问题，设置标志位不好使？？？？
        self.list_id = self.enumProcesses()
        self.check_out.set('浏览器已关闭，可以继续')     #开启关闭处的提示
        try:
            for id in self.list_id:
                print id
                os.popen('taskkill.exe /pid:'+str(id)) 
        except OSError as msg:
            print msg 
        print self.pid,'self.pid'
        #os.popen('taskkill.exe /pid:'+str(self.pid))    ##os.kill(self.id,SIGKILL)
    def test_end(self):  ##界面上停止按钮调用函数，使用多线程同时定制功能运行，界面可操作功能启用
        self.check_out.set('浏览器已关闭，可以继续') 
        threads = []
        t1 = threading.Thread(target=self.all_enable)
        threads.append(t1)
        t2 =threading.Thread(target=self.set_stop)
        threads.append(t2)
        t3 = threading.Thread(target=self.check_log)
        threads.append(t3)
        for t in threads:
            t.setDaemon(True)
            t.start()
        #t.join()
        
    def view_results(self):    ##界面上结果查看按钮，弹出报告结果。。。。。待实现
        print "Viewing Results"

    def combox1(self):     ##定义Combobox时间函数。。。。。待实现
        print self.Tabs_Conf2_fun_list1.get()
        '''
        if self.Tabs_Conf2_fun_list1.get()=='图像调节':
            print '1'                         ###可以换成函数
        elif self.Tabs_Conf2_fun_list1.get()=='曝光':
            print '2'
        else:
            print '3'
        '''
    def createWidgets(self):
        self.top = self.winfo_toplevel()           #下面2个不知道干嘛用的，浪费
        self.style = Style()
        self.top= Label(self.top,text="欢迎使用KIPC功能自动化测试",font=("Arial",16))          #欢迎词
        self.top.place(relx=0.2,rely=0.02)
        ################################第一个标签#############################################
        self.Tabs = Notebook()          #定义一个Notebook类型以及标签1业务里面的值
        self.Tabs.place(relx=0.00, rely=0.07, relwidth=1.01, relheight=1)
        self.Tabs_Func = Frame(self.Tabs)
        self.Tabs.add(self.Tabs_Func, text='业务')
        #定义标签1业务里面功能选择，LabelFrame
        self.Tabs_Func1 = Label(self.Tabs_Func,text="功能项选择",font=("System",8) )
        self.Tabs_Func1.place(relx=0.00,rely=0.01)
        self.group_Fun1 = tk.LabelFrame(self.Tabs_Func,height = 80,width = 760,text="图像功能",font=("System",10) )
        self.group_Fun1.place(relx=0.02,rely=0.06) 
        self.group_Fun2 = tk.LabelFrame(self.Tabs_Func,height = 60,width = 760,text="音/视频",font=("System",10) )
        self.group_Fun2.place(relx=0.02,rely=0.21)    
        self.group_Fun3 = tk.LabelFrame(self.Tabs_Func,height = 45,width = 760,text="云台/OSD",font=("System",10) )
        self.group_Fun3.place(relx=0.02,rely=0.32)    
        self.group_Fun4 = tk.LabelFrame(self.Tabs_Func,height = 60,width = 760,text="系统相关",font=("System",10) )
        self.group_Fun4.place(relx=0.02,rely=0.41) 
        self.group_Fun5 = tk.LabelFrame(self.Tabs_Func,height = 60,width = 760,text="其他",font=("System",10) )
        self.group_Fun5.place(relx=0.02,rely=0.52) 
        self.group_Fun6 = tk.LabelFrame(self.Tabs_Func,height = 50,width = 760,text="信息显示",font=("Arial",10) )
        self.group_Fun6.place(relx=0.02,rely=0.63) 
        #定义LabelFrame业务里面功能选择
        self.Tabs_Func1_gntx1 = tk.Checkbutton(self.group_Fun1,text="图像调节",variable=self.v1,onvalue = '1',offvalue ='0',state='active',command = self.choice_v1)
        self.Tabs_Func1_gntx1.select()
        self.Tabs_Func1_gntx1.place(relx=0.08,rely=0.00)  #relx指定该组件相对于父组件的水平位置,rely指定该组件相对于父组件的垂直位置
        self.Tabs_Func1_gntx2 = tk.Checkbutton(self.group_Fun1,text="曝光",variable=self.v2,onvalue = '2',offvalue ='0',state='active',command = self.choice_v2)
        self.Tabs_Func1_gntx2.select()
        self.Tabs_Func1_gntx2.place(relx=0.21,rely=0.00)  
        self.Tabs_Func1_gntx3 = tk.Checkbutton(self.group_Fun1,text="白平衡",variable=self.v3,onvalue = '3',offvalue ='0',state='active',command = self.choice_v3)
        self.Tabs_Func1_gntx3.select()
        self.Tabs_Func1_gntx3.place(relx=0.33,rely=0.00)
        self.Tabs_Func1_gntx4 = tk.Checkbutton(self.group_Fun1,text="日夜转换",variable=self.v4,onvalue = '4',offvalue ='0',state='active',command = self.choice_v4)
        self.Tabs_Func1_gntx4.deselect()
        self.Tabs_Func1_gntx4.place(relx=0.46,rely=0.00)
        self.Tabs_Func1_gntx5 = tk.Checkbutton(self.group_Fun1,text="图像增强",variable=self.v5,onvalue = '5',offvalue ='0',state='active',command = self.choice_v5)
        self.Tabs_Func1_gntx5.deselect()
        self.Tabs_Func1_gntx5.place(relx=0.59,rely=0.00)
        self.Tabs_Func1_gntx6 = tk.Checkbutton(self.group_Fun1,text="防抖",variable=self.v6,onvalue = '6',offvalue ='0',state='active',command = self.choice_v6)
        self.Tabs_Func1_gntx6.deselect()
        self.Tabs_Func1_gntx6.place(relx=0.72,rely=0.00)
        self.Tabs_Func1_gntx7 = tk.Checkbutton(self.group_Fun1,text="翻转与回显",variable=self.v7,onvalue = '7',offvalue ='0',state='active',command = self.choice_v7)
        self.Tabs_Func1_gntx7.deselect()
        self.Tabs_Func1_gntx7.place(relx=0.85,rely=0.00)
        ##以下为未实现功能
        self.Tabs_Func1_gntx8 = tk.Checkbutton(self.group_Fun1,text="聚焦",variable=self.mv,offvalue ='off',state='disabled',command = self.callbutton)
        self.Tabs_Func1_gntx8.deselect()
        self.Tabs_Func1_gntx8.place(relx=0.08,rely=0.45)  
        self.Tabs_Func1_gntx9 = tk.Checkbutton(self.group_Fun1,text="红外",variable=self.mv,offvalue ='off',state='disabled',command = self.callbutton)
        self.Tabs_Func1_gntx9.deselect()
        self.Tabs_Func1_gntx9.place(relx=0.21,rely=0.4)  
        self.Tabs_Func1_gntx10 = tk.Checkbutton(self.group_Fun1,text="待实现",variable=self.mv,offvalue ='off',state='disabled',command = self.callbutton)
        self.Tabs_Func1_gntx10.deselect()
        self.Tabs_Func1_gntx10.place(relx=0.33,rely=0.4)  
        self.Tabs_Func1_gntx11 = tk.Checkbutton(self.group_Fun1,text="待实现",variable=self.mv,offvalue ='off',state='disabled',command = self.callbutton)
        self.Tabs_Func1_gntx11.deselect()
        self.Tabs_Func1_gntx11.place(relx=0.46,rely=0.4)        
        self.Tabs_Func1_gntx12 = tk.Checkbutton(self.group_Fun1,text="待实现",variable=self.mv,offvalue ='off',state='disabled',command = self.callbutton)
        self.Tabs_Func1_gntx12.deselect()
        self.Tabs_Func1_gntx12.place(relx=0.59,rely=0.4)
        self.Tabs_Func1_gntx13 = tk.Checkbutton(self.group_Fun1,text="待实现",variable=self.mv,offvalue ='off',state='disabled',command = self.callbutton)
        self.Tabs_Func1_gntx13.deselect()
        self.Tabs_Func1_gntx13.place(relx=0.72,rely=0.4)
        self.Tabs_Func1_gntx14 = tk.Checkbutton(self.group_Fun1,text="待实现",variable=self.mv,offvalue ='off',state='disabled',command = self.callbutton)
        self.Tabs_Func1_gntx14.deselect()
        self.Tabs_Func1_gntx14.place(relx=0.85,rely=0.4)
        ##定义第一LabelFrame里面的全选和取消按钮，函数未实现。。。。。待研究实现逻辑
        self.Tabs_Func1_gntx19 = Radiobutton(self.group_Fun1,text="全选",state='active',command=self.all_value)
        self.Tabs_Func1_gntx19.place(relx=0.00,rely=0.00)
        self.Tabs_Func1_gntx20 = Radiobutton(self.group_Fun1,text="取消",state='active',command=self.notall_value)
        self.Tabs_Func1_gntx20.place(relx=0.00,rely=0.5)
        #定义开始、停止、和结果查看按钮
        self.Tabs_Func1_zx1 = Button(self.Tabs_Func,text="开始", command=self.test_begin)
        self.Tabs_Func1_zx1.place(relx=0.22,rely=0.79)
        self.Tabs_Func1_zx2 = Button(self.Tabs_Func,text="停止",command=self.test_end)
        self.Tabs_Func1_zx2.place(relx=0.42,rely=0.79)  
        self.Tabs_Func1_zx3 = Button(self.Tabs_Func,text="结果查看",command=self.view_results)
        self.Tabs_Func1_zx3.place(relx=0.62,rely=0.79) 
        ##定义信息显示的label
        self.Tabs_Func1_out = Label(self.group_Fun6,textvariable=self.check_out )
        self.Tabs_Func1_out.place(relx=0.00,rely=0.00)

        ################################第二个标签#############################################
        self.Tabs_Conf = Frame(self.Tabs)
        self.Tabs.add(self.Tabs_Conf, text='配置')    #定义标签2配置里面的值
        #定义标签2配置里面：IP用户名密码的信息       
        self.Tabs_Conf_group1 = tk.LabelFrame(self.Tabs_Conf,height = 110,width = 760,text="基础配置",font=("System",10) )
        self.Tabs_Conf_group1.place(relx=0.02,rely=0.02) 
        self.Tabs_Conf1_ip=Label(self.Tabs_Conf_group1,text="IP地址:").place(relx=0.02,rely=0.02)
        self.Tabs_Conf1_ip_entry=Entry(self.Tabs_Conf_group1,textvariable=self.host)
        self.Tabs_Conf1_ip_entry.place(relx=0.1,rely=0.02,relwidth=0.2)
        self.Tabs_Conf1_user=Label(self.Tabs_Conf_group1,text="用户名：").place(relx=0.37,rely=0.02)
        self.Tabs_Conf1_user_spinbox=Spinbox(self.Tabs_Conf_group1,values= ("admin"),state='disabled',buttondownrelief='flat').place(relx=0.44,rely=0.02,relwidth=0.08)
        self.Tabs_Conf1_passwd=Label(self.Tabs_Conf_group1,text="密码:").place(relx=0.65,rely=0.02)
        self.Tabs_Conf1_passwd_entry=Entry(self.Tabs_Conf_group1,textvariable=self.password)
        self.Tabs_Conf1_passwd_entry.place(relx=0.7,rely=0.02)
        self.Tabs_Conf1_firefox=Label(self.Tabs_Conf_group1,text="Firefox路径:").place(relx=0.02,rely=0.36)
        self.Tabs_Conf1_firefox_entry=Entry(self.Tabs_Conf_group1,textvariable=self.profiledir)
        self.Tabs_Conf1_firefox_entry.place(relx=0.14,rely=0.36,relwidth=0.7)
        self.Tabs_Conf1_logpath=Label(self.Tabs_Conf_group1,text="日志保存路径:").place(relx=0.02,rely=0.68)
        self.Tabs_Conf1_logpath_entry=Entry(self.Tabs_Conf_group1,textvariable=self.log_path)
        self.Tabs_Conf1_logpath_entry.place(relx=0.15,rely=0.68,relwidth=0.4)
        self.Tabs_Conf1_save = Button(self.Tabs_Conf_group1,text="保存",command=self.cfsave)
        self.Tabs_Conf1_save.place(relx=0.92,rely=0.60,relwidth=0.06)
        #定义标签2配置里面：id库信息
        self.Tabs_Conf_group2 = tk.LabelFrame(self.Tabs_Conf,height = 380,width = 760,text="高级配置（开发人员使用，未实现）",font=("System",10) )
        self.Tabs_Conf_group2.place(relx=0.02,rely=0.23) 
        ##ID库及高级操作
        self.Tabs_Conf_group2_id = tk.LabelFrame(self.Tabs_Conf_group2,height = 110,width = 740,text="ID库",font=("System",10) )
        self.Tabs_Conf_group2_id.place(relx=0.01,rely=0.01) 
        self.Tabs_Conf_group2_fun = tk.LabelFrame(self.Tabs_Conf_group2,height = 230,width = 740,text="函数相关",font=("System",10) )
        self.Tabs_Conf_group2_fun.place(relx=0.01,rely=0.33) 
        ##ID查询
        self.Tabs_Conf2_ids=Label(self.Tabs_Conf_group2_id,text="ID查询：").place(relx=0.01,rely=0.01)
        self.number = tk.StringVar()
        self.Tabs_Conf2_ldlist1=Combobox(self.Tabs_Conf_group2_id,textvariable=self.number,state='readonly')
        self.Tabs_Conf2_ldlist1['values'] = ('实时浏览', '录像回放', '图片管理', '配置') 
        self.Tabs_Conf2_ldlist1.place(relx=0.08,rely=0.02,relwidth=0.1)
        self.Tabs_Conf2_ldlist1.current(3) 
        self.Tabs_Conf2_save1 = Button(self.Tabs_Conf_group2_id,text="查询",command=self.callbutton)
        self.Tabs_Conf2_save1.place(relx=0.92,rely=0.02,relwidth=0.06)
        ##ID修改
        self.Tabs_Conf2_idrn=Label(self.Tabs_Conf_group2_id,text="ID修改：").place(relx=0.01,rely=0.38)
        self.Tabs_Conf2_save1 = Button(self.Tabs_Conf_group2_id,text="修改",command=self.callbutton)
        self.Tabs_Conf2_save1.place(relx=0.92,rely=0.35,relwidth=0.06)
        ##ID增加
        self.Tabs_Conf2_idadd=Label(self.Tabs_Conf_group2_id,text="ID增加：").place(relx=0.01,rely=0.72)       
        self.Tabs_Conf2_save1 = Button(self.Tabs_Conf_group2_id,text="增加",command=self.callbutton)
        self.Tabs_Conf2_save1.place(relx=0.82,rely=0.68,relwidth=0.06)
        self.Tabs_Conf2_save1 = Button(self.Tabs_Conf_group2_id,text="自动获取",command=self.callbutton)
        self.Tabs_Conf2_save1.place(relx=0.90,rely=0.68,relwidth=0.1)
        ##高级操作相关
        ####浏览器选择（考虑是否实现）
        #
        ###
        
        ####测试用例----选择后进行查询，将查询值在下一个框中显示
        self.Tabs_Conf2_fun_l1=Label(self.Tabs_Conf_group2_fun,text="测试用例：").place(relx=0.01,rely=0.02)
        self.num1 = tk.StringVar()
        self.Tabs_Conf2_fun_list1=Combobox(self.Tabs_Conf_group2_fun,textvariable=self.num1,state='readonly')
        self.Tabs_Conf2_fun_list1['values'] = ('图像调节', '曝光', '图像增强', '防抖') 
        self.Tabs_Conf2_fun_list1.bind('<<ComboboxSelected>>', self.combox1)   ##'<<ComboboxSelected>>'选中事件
        self.Tabs_Conf2_fun_list1.current(0)   ##默认显示列表第几个
        self.Tabs_Conf2_fun_list1.place(relx=0.1,rely=0.02,relwidth=0.1)   

        #####显示上一级Combobox选择后显示数值
        self.Tabs_Conf2_fun_l2=Label(self.Tabs_Conf_group2_fun,text="测试子项：").place(relx=0.23,rely=0.02)
        self.num2 = tk.StringVar()
        self.Tabs_Conf2_fun_list2=Combobox(self.Tabs_Conf_group2_fun,textvariable=self.num2,state='readonly')
        self.Tabs_Conf2_fun_list2['values'] = ('亮度', '对比度', '饱和度', '锐度') 
        self.Tabs_Conf2_fun_list2.place(relx=0.33,rely=0.02,relwidth=0.1)
        self.Tabs_Conf2_fun_list2.current(0) 
        #####显示上一级Combobox选择后显示数值
        self.Tabs_Conf2_fun_l3=Label(self.Tabs_Conf_group2_fun,text="定位方法：").place(relx=0.45,rely=0.02)
        self.num3 = tk.StringVar()
        self.Tabs_Conf2_fun_list3=Combobox(self.Tabs_Conf_group2_fun,textvariable=self.num3,state='readonly')
        self.Tabs_Conf2_fun_list3['values'] = ('By_id', 'By_name', 'By_class', 'By_Xpath','By_CSS') 
        self.Tabs_Conf2_fun_list3.place(relx=0.53,rely=0.02,relwidth=0.1)
        self.Tabs_Conf2_fun_list3.current(0) 
        #####显示上一级Combobox选择后显示数值
        self.Tabs_Conf2_fun_l4=Label(self.Tabs_Conf_group2_fun,text="测试值：").place(relx=0.65,rely=0.02)
        self.Tabs_Conf2_fun_en1=Entry(self.Tabs_Conf_group2_fun,textvariable=self.getvalue)
        self.Tabs_Conf2_fun_en1.place(relx=0.73,rely=0.02,relwidth=0.2)
        
    def common_disable(self):
        self.Tabs_Func1_gntx1.config(state="disable")
        self.Tabs_Func1_gntx2.config(state="disable")
        self.Tabs_Func1_gntx3.config(state="disable")
        self.Tabs_Func1_gntx4.config(state="disable")
        self.Tabs_Func1_gntx5.config(state="disable")
        self.Tabs_Func1_gntx6.config(state="disable")
        self.Tabs_Func1_gntx7.config(state="disable")
        self.Tabs_Conf1_ip_entry.config(state="disable")
        self.Tabs_Conf1_passwd_entry.config(state="disable")
        self.Tabs_Conf1_firefox_entry.config(state="disable")
        self.Tabs_Conf1_logpath_entry.config(state="disable")

    def common_enable(self):
        self.Tabs_Func1_gntx1.config(state="normal")
        self.Tabs_Func1_gntx2.config(state="normal")
        self.Tabs_Func1_gntx3.config(state="normal")
        self.Tabs_Func1_gntx4.config(state="normal")
        self.Tabs_Func1_gntx5.config(state="normal")
        self.Tabs_Func1_gntx6.config(state="normal")
        self.Tabs_Func1_gntx7.config(state="normal")
        self.Tabs_Conf1_ip_entry.config(state="normal")
        self.Tabs_Conf1_passwd_entry.config(state="normal")
        self.Tabs_Conf1_firefox_entry.config(state="normal")
        self.Tabs_Conf1_logpath_entry.config(state="normal")

    def start_disable(self):
        self.common_disable()
        self.Tabs_Func1_zx1.config(state="disable") #开始
        self.Tabs_Func1_zx2.config(state="normal") #停止
        self.Tabs_Func1_zx3.config(state="disable") #分析
    def all_enable(self):
        self.common_enable()
        self.Tabs_Func1_zx1.config(state="normal") #开始
        self.Tabs_Func1_zx2.config(state="normal") #停止
        self.Tabs_Func1_zx3.config(state="normal") #分析
    def all_disable(self):
        self.common_disable()
        self.Tabs_Func1_zx1.config(state="disable") #开始
        self.Tabs_Func1_zx2.config(state="disable") #停止
        self.Tabs_Func1_zx3.config(state="disable") #分析
if __name__ == "__main__":
    top = Tk()
    GUID = GUI()
    GUID.__init__()
    top.mainloop()
    