# coding=utf-8
#_author_='wuweibin'
#_time_='2016/4/13'
import ConfigParser,sys,os
from runtest.test_aImagsSettings import Imageseting

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
    def fun_dict(self):
        self.fun01=self.fun1.test_01
        self.fun02=self.fun1.test_02
        self.fun03=self.fun1.test_03
        self.fun04=self.fun1.test_04
        self.fun05=self.fun1.test_05
        self.fun06=self.fun1.test_06
        self.fun07=self.fun1.test_07
        self.fun_runlist = []
        self.fun_dict1={'1':self.fun01,'2':self.fun02,'3':self.fun03,'3':self.fun03,'4':self.fun04,'5':self.fun05,'6':self.fun06,'7':self.fun07}
        for i in self.fun_list:
            print i  
            self.fun_runlist.append(self.fun_dict1.get( i))
            try:
                self.fun_dict1.get( i)()
            except Exception as e:
                print e
                pass
            print 'end fun_dict'
        self.fun1.quitfirefox()

if __name__ == "__main__":
    t = Run_Test()
    t.stop_firefox()