#coding:utf-8
#!/usr/bin/env python
##################################################################
#定义、读取config目录下excel中case的value值
#在excel中添加新的case、valuse，需要在下面定义*_list和后面的读取的列数
#2016-05-3修改
##################################################################
import xlrd,os

dirpwd = os.path.abspath('.') 
#print "测试用例所在目录绝度路径"+dirpwd
excelname = r'%s\IPC_v7_message.xlsx' %dirpwd
#print "测试用例excel路径"+excelname
opensheet = xlrd.open_workbook(excelname)

def getdata(value):     ##获取excel中“行”的值，并处理空值
    table = opensheet.sheet_by_name("aVideoCameracase")
    test=table.row_values(value)
    data = test[5:-1]
    while ''  in data:
        data1=data.remove('') 
    return data
    print data1
    
light_list = getdata(1)      #亮度
contrast_list = getdata(2)    ##对比度
saturation_list = getdata(3)     ##饱和度
sharpness_list = getdata(4)     ##锐度

GainMode_list = getdata(5)  ##增益模式
gainmax_value_list = getdata(6)  ##自动--增益上限
gainlevel_value_list = getdata(7)  ##手动---增益等级
IrisType_list = getdata(8)  ##光圈模式
irislevel_value_list = getdata(9)  ##自动---光圈灵敏度
irissize_value_list = getdata(10)  ##手动---光圈大小
ShuterMode_list = getdata(11) ##快门模式
Shutermin_list = getdata(12)  ##自动---快门下限
Shutterlevel_list = getdata(13)  ##手动---快门等级
AntiFlickerMode_list = getdata(14)  ##防闪烁

WhiteBalance_list = getdata(15)  ##白平衡
R_value_list = getdata(16)    ##手动白平衡R_value
B_value_list = getdata(17)    ##手动白平衡B_value

IrcutfilterType_list = getdata(18)     ##日夜切换模式
daytonightlevel_value_list = getdata(19)   ##日夜转换灵敏度
daytonight_value_list = getdata(20)    ##日夜转换等待时间
threshold_value_list = getdata(21)   ##日夜转换阈值

mode2d_list = getdata(22)      ##2D降噪模式
D2_value_list = getdata(23)     ##2D降噪
mode3d_list = getdata(24)     ##3D降噪模式
D3_value_list = getdata(25)      ##3D降噪
backlightmode_list = getdata(26)     ##动态调节
imageenhance_slect_list = getdata(27)     ##图像增强
selectassistmalf_list = getdata(28)     ##畸变校正

ModeAntishake_list = getdata(29)    ##防抖
antishake_value_list = getdata(30)    ##防抖等级
 
selectRotateMode_list = getdata(31)   ##翻转模式
corridormode_list = getdata(32)  ##手动--走廊模式
imagemode_list = getdata(33)   ##手动--镜像模式
cvbsmode_list = getdata(34)   ##本地回显

videoResolution_list = getdata(39)   ##主流分辨率
videoResolution1_list = getdata(40)  ##辅流码率
maxFrameRate_list = getdata(43)   ##帧率
constantBitRate_list = getdata(44)   ##码率

if __name__ =='__main__':
    print  sharpness_list,contrast_list



