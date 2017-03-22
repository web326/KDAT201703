#coding:utf-8
#!/usr/bin/env python
#*************************************************************************************************
#图像调节部分功能测试
#2016-07-29修改
#***************************************************************************************************
import unittest,os
from api import getcasevalue,verifycmd,operation_verify
from HTMLTestRunner import *
from api.operation_verify import operation,Loginipc
from api.menupage import MenuPage
from api.common import ComAction
from api.common  import *
from api.messages import Getipcmessage
from Canvas import Line

globle_n = 1

class Imageseting(operation): 
    def __init__(self):
        self.logdir = logdir
        print self.logdir
        cfg = Getipcmessage()
        ip = cfg.getcfgip()
        username = cfg.getcfgusername()
        password = cfg.getcfgpassword()
        self.loginIPC(ip,username,password)
        entermenu =self.aImagsSettings()
    def test_01(self):
        '''<配置---摄像机---图像>---图像调节'''
        time.sleep(2)
        try:
            self.operation_sendkeys(getcasevalue.light_list,'亮度调节', verifycmd.cmd2,*self.lightness_value_loc)
        except Exception as e:
            print e
            pass
        try:
            self.operation_sendkeys(getcasevalue.contrast_list, '对比度调节', verifycmd.cmd3,*self.contrast_value_loc)
        except Exception as e:
            print e
            pass
        try:
            self.operation_sendkeys(getcasevalue.saturation_list, '饱和度调节', verifycmd.cmd4,*self.saturation_value_loc)
        except Exception as e:
            print e
            pass
        try:
            self.operation_sendkeys(getcasevalue.sharpness_list, '锐度调节', verifycmd.cmd5,*self.sharpness_value_loc)
        except Exception as e:
            print e
            pass
    def test_02(self):
        '''<配置---摄像机---图像>---曝光'''
        self.clickID(*self.exposureh5_loc)
        time.sleep(1)
        try:
            self.operation_select(['manual'], '增益模式:手动', verifycmd.cmd6,*self.GainMode_loc)
            self.operation_sendkeys(getcasevalue.gainlevel_value_list, '增益等级', verifycmd.cmd8,*self.gainlevel_value_loc)
        except Exception as e:
            print e
            pass
        try:
            self.operation_select(['auto'], '增益模式：自动', verifycmd.cmd6,*self.GainMode_loc)
            self.operation_sendkeys(getcasevalue.gainmax_value_list, '增益上限', verifycmd.cmd7,*self.gainmax_value_loc)   
        except Exception as e:
            print e
            pass
        try:
            self.operation_select(['p_irismanual'], '光圈模式：P_IRIS手动', verifycmd.cmd9,*self.IrisType_loc)
        except Exception as e:
            print e
            pass
        try:
            self.operation_select(['dc_irismanual'], '光圈模式：DC_IRIS手动', verifycmd.cmd9,*self.IrisType_loc)
            self.operation_sendkeys(getcasevalue.irissize_value_list, '光圈大小', verifycmd.cmd11,*self.irissize_value_loc)
        except Exception as e:
            print e
            pass
        try:
            self.operation_select(['dc_irisauto'], '光圈模式：DC_IRIS自动', verifycmd.cmd9,*self.IrisType_loc)
            self.operation_sendkeys(getcasevalue.irislevel_value_list, '光圈灵敏度', verifycmd.cmd10,*self.irislevel_value_loc)
        except Exception as e:
            print e
            pass
        try:
            self.operation_select(['manual'], '快门模式：手动', verifycmd.cmd12,*self.ShuterMode_loc)
            self.operation_select(getcasevalue.Shutterlevel_list, '快门等级', verifycmd.cmd14,*self.Shutterlevel_loc)
        except Exception as e:
            print e
            pass
        try:
            self.operation_select(['auto'], '快门模式：自动', verifycmd.cmd12,*self.ShuterMode_loc)
            self.operation_select(getcasevalue.Shutermin_list, '快门下限', verifycmd.cmd13,*self.Shutermin_loc)  
        except Exception as e:
            print e
            pass
        try:
            self.operation_select(getcasevalue.AntiFlickerMode_list, '防闪烁', verifycmd.cmd15,*self.AntiFlickerMode_loc)
        except Exception as e:
            print e
            pass

    def test_03(self):
        '''<配置---摄像机---图像>---白平衡'''
        try:
            self.clickID(*self.whiteblanceh5_loc)
            self.operation_select(getcasevalue.WhiteBalance_list, '白平衡', verifycmd.cmd16,*self.WhiteBalance_loc)
            self.operation_select(['manual'],'手动白平衡', verifycmd.cmd16,*self.WhiteBalance_loc)   
            self.operation_sendkeys(getcasevalue.R_value_list, '手动白平衡R值', verifycmd.cmd17,*self.R_value_loc)
            self.operation_sendkeys(getcasevalue.B_value_list, '手动白平衡B值', verifycmd.cmd18,*self.B_value_loc)
        except Exception as e:
            print e
            pass
        try:
            self.operation_select(['auto1'],'自动白平衡1', verifycmd.cmd16,*self.WhiteBalance_loc) 
            self.clickID(*self.whiteblanceh5_loc)
        except Exception as e:
            print e
            pass
    def test_04(self):
        '''<配置---摄像机---图像>---日夜转换'''
        self.clickID(*self.ircutfilterh5_loc)
        self.operation_select(getcasevalue.IrcutfilterType_list, '日夜切换', verifycmd.cmd1,*self.IrcutfilterType_loc)
        self.operation_sendkeys(getcasevalue.daytonightlevel_value_list, '日夜转换灵敏度', verifycmd.cmd19,*self.daytonightlevel_value_loc)
        self.operation_sendkeys(getcasevalue.daytonight_value_list, '日夜转换等待时间', verifycmd.cmd21,*self.daytonight_value_loc)
        self.operation_sendkeys(getcasevalue.threshold_value_list, '日夜转换阈值', verifycmd.cmd20,*self.threshold_value_loc)
        self.clickID(*self.ircutfilterh5_loc)
    def test_05(self):
        '''<配置---摄像机---图像>---图像增强'''
        self.clickID(*self.ImageEnhancementh5_loc)
        try:
            self.operation_select(getcasevalue.mode2d_list, '2D降噪模式切换', verifycmd.cmd22,*self.mode2d_loc)
            self.operation_sendkeys(getcasevalue.D2_value_list, '2D降噪数值', verifycmd.cmd23,*self.D2_value_loc)
        except Exception as e:
            print e
            pass
        self.operation_select(getcasevalue.mode3d_list, '3D降噪模式切换', verifycmd.cmd24,*self.mode3d_loc)
        self.operation_sendkeys(getcasevalue.D3_value_list, '3D降噪数值', verifycmd.cmd25,*self.D3_value_loc)
        self.operation_select(getcasevalue.backlightmode_list, '动态调节', verifycmd.cmd26,*self.backlightmode_loc)
        self.operation_select(getcasevalue.imageenhance_slect_list, '图像增强', verifycmd.cmd30,*self.imageenhance_slect_loc)
        try:
            self.operation_select(getcasevalue.selectassistmalf_list, '畸变校正', verifycmd.cmd32,*self.selectassistmalf_loc)
        except Exception as e:
            print e
            pass
    def test_06(self):
        '''<配置---摄像机---图像>---防抖'''
        try:
            self.clickID(*self.Antishake5_loc)
            self.operation_select(['open'], '防抖模式', verifycmd.cmd33,*self.ModeAntishake_loc)
            self.operation_sendkeys(getcasevalue.antishake_value_list, '防抖等级', verifycmd.cmd34,*self.antishake_value_loc)
            self.operation_select(['close'], '防抖模式', verifycmd.cmd33,*self.ModeAntishake_loc)
        except Exception as e:
            print e
            pass
    def test_07(self):
        '''<配置---摄像机---图像>---图像翻转与回显'''
        try:
            self.clickID(*self.otherh5_loc)
            self.operation_select(['manual'], '图像翻转模式手动', verifycmd.cmd33,*self.selectRotateMode_loc)
            self.operation_select(getcasevalue.corridormode_list, '走廊模式', verifycmd.cmd34,*self.corridormode_loc)
            self.operation_select(getcasevalue.imagemode_list, '图像翻转', verifycmd.cmd34,*self.imagemode_loc)
            self.operation_select(['auto'], '图像翻转模式', verifycmd.cmd33,*self.selectRotateMode_loc)
            self.operation_select(getcasevalue.cvbsmode_list, '本地回显', verifycmd.cmd33,*self.cvbsmode_loc)
        except Exception as e:
            print e
            pass

    def quitfirefox(self):
        self.driver.quit()
        self.printlog('IPCV7自动化结束测试')

if __name__ == '__main__':
    t = Imageseting()
    t.test_01()