# coding=utf-8
#_author_='wuweibin'
#_time_='2016/4/13'
import ConfigParser,sys,os
#from runtest import day_night
from runtest.test_aImagsSettings import Imageseting
globle_n = 1
class Run_Test():
    def __init__(self):
        self.fun1 = Imageseting()
        sys.path.append('.\runtest')
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(r'Config.ini')
        self.fun_list1=self.cf.items("fun")
        self.fun_list = []
        for i in self.fun_list1:
            if int(i[1]) !=0:
                self.fun_list.append(i[1])
            else:
                pass
        self.fun_list.sort(key=lambda x:x[0])
    def stop_firefox(self):
        #self.tid = ctypes.
        print 'self.tid'
    def fun_dict(self):
        self.fun01=self.fun1.test_01
        self.fun02=self.fun1.test_02
        self.fun03=self.fun1.test_03
        self.fun_runlist = []
        #print 'start fun_dict'
        self.fun_dict1={'1':self.fun01,'2':self.fun02,'3':self.fun03}
        #print 'fun_dict1',self.fun_dict1
        while (0<globle_n<2):
            print 'globle_n:::::',globle_n
            for i in self.fun_list:
                print i  
                self.fun_runlist.append(self.fun_dict1.get( i))
                self.fun_dict1.get( i)()
            print 'end fun_dict'
        self.fun1.quitfirefox()
if __name__ == "__main__":
    t = Run_Test()
    t.stop_firefox()

'''
import re,os,sys,api
from HTMLTestRunner import *
from api.common import LogResultDir
path = os.path.abspath(os.path.dirname(sys.argv[0]))
print 'path'+':'+path
##sys.argv[0]表示代码本身文件路径；os.path.dirname去掉文件名，返回目录路径；os.path.abspath获取绝对路径
files = os.listdir(path)    ##获得指定目录中的内容
test = re.compile('test_aImagsSettings.py$')
#print test
##re.compile(pattern[, flags])，把一个正则表达式pattern编译成正则对象，以便可以用正则对象的match和search方法
files = filter(test.search, files)     ## 搜索正则表达式
print files
filenameToModuleName = lambda f: os.path.splitext(f)[0]   ##lambda为匿名函数，分离文件名
#print filenameToModuleName
moduleNames = map(filenameToModuleName, files)    ##作用是将一个列表映射到另一个列表 
modules = map(__import__, moduleNames)                        ##把分离的测试用例全部导进来
load = unittest.defaultTestLoader.loadTestsFromModule   ##
suit=unittest.TestSuite(map(load, modules))
print suit
#result=unittest.TextTestRunner(verbosity=2).run(suit)
logp=LogResultDir()
resultpath = logp.resultdir()
ISOTIMEFORMAT='%Y%m%d%H%M%S'
resultname= resultpath+'\\'+time.strftime(ISOTIMEFORMAT,time.localtime())+'result.html'
fp = open(resultname, 'wb')
runner = HTMLTestRunner(stream=fp,
                            title='IPC V7自动化测试（Python+Selenium 2.0）测试报告',
                            description='IPCv7自动化测试环境： win7，浏览器：Firefox ，测试组织：中试')
runner.run(suit)
'''