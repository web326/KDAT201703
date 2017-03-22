#coding:utf-8
#!/usr/bin/env python
##################################################################
#定义ssh到IPC获取配置文件shell命令
#2016-05-3修改
##################################################################
    ##1.读取配置文件--->日夜模式值
cmd1 = ["cat /usr/config/ipccfg.conf|awk -F DayNightMode '{print $5}'|awk -F , '{print $1"" }'|awk -F : '{print $2}'"]
    ##2.读取配置文件--->亮度
cmd2 = ["cat /usr/config/ipccfg.conf|awk -F Brightness '{print $4}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##3.读取配置文件--->对比度
cmd3 = [ "cat /usr/config/ipccfg.conf|awk -F Contrast '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##4.读取配置文件--->饱和度
cmd4 = ["cat /usr/config/ipccfg.conf|awk -F Saturation '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##5.读取配置文件--->锐度
cmd5 = ["cat /usr/config/ipccfg.conf|awk -F Sharpness '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]

    ##6.读取配置文件--->曝光---增益模式  auto 1，manual 0
cmd6 = ["cat /usr/config/ipccfg.conf|awk -F GainMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##7.读取配置文件--->曝光---增益上限（自动 ）
cmd7 = ["cat /usr/config/ipccfg.conf|awk -F GainMax '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##8.读取配置文件--->曝光---增益等级（手动）
cmd8 = ["cat /usr/config/ipccfg.conf|awk -F GainLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##9.读取配置文件--->曝光--光圈模式 （DC-IRIS自动dc_irisauto  1；DC-IRIS手动dc_irismanual 0；P-IRIS手动p_irismanual  2）
cmd9 = ["cat /usr/config/ipccfg.conf|awk -F IrisMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##10.读取配置文件--->曝光--光圈灵敏度 （DC-IRIS自动模式）
cmd10 = ["cat /usr/config/ipccfg.conf|awk -F IrisSensitivety '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##11.读取配置文件--->曝光--光圈大小 （DC-IRIS手动模式）
cmd11 = ["cat /usr/config/ipccfg.conf|awk -F IrisLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##12.读取配置文件--->曝光---快门模式（auto 1；manual 0）
cmd12 = ["cat /usr/config/ipccfg.conf|awk -F ShutterMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##13.读取配置文件--->曝光---快门下限（快门自动模式）
cmd13 = ["cat /usr/config/ipccfg.conf|awk -F ShutterMin '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##14.读取配置文件--->曝光---快门等级（快门手动模式）
cmd14 = ["cat /usr/config/ipccfg.conf|awk -F ShutterTime '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##15.读取配置文件--->曝光---防闪烁（50Hz 0；60Hz 1，自然光 2）
cmd15 = ["cat /usr/config/ipccfg.conf|awk -F FrequencyMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]

    ##16.读取配置文件--->白平衡模式
cmd16 = ["cat /usr/config/ipccfg.conf|awk -F WhiteBalMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##17.读取配置文件--->手动白平衡模式R-Value
cmd17 = ["cat /usr/config/ipccfg.conf|awk -F WhiteBalRed '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##18.读取配置文件--->手动白平衡模式B-Value
cmd18 = ["cat /usr/config/ipccfg.conf|awk -F WhiteBalanceBlue '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]

    ##19.读取配置文件--->日夜切换---灵敏度
cmd19 = ["cat /usr/config/ipccfg.conf|awk -F DayToNightSensityLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##20.读取配置文件--->日夜切换----转换阈值
cmd20 = ["cat /usr/config/ipccfg.conf|awk -F DayToNightThresholdValue '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##21.读取配置文件--->日夜转换---等待时间
cmd21 = ["cat /usr/config/ipccfg.conf|awk -F DayToNightDelayTime '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]

    ##22.读取配置文件--->2d降噪模式
cmd22 = ["cat /usr/config/ipccfg.conf|awk -F 2DNoiseReduceMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##23.读取配置文件--->2d降噪
cmd23 = ["cat /usr/config/ipccfg.conf|awk -F 2DNoiseReduceLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##24.读取配置文件--->3d降噪模式
cmd24 = ["cat /usr/config/ipccfg.conf|awk -F 3DNoiseReduceMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##25.读取配置文件--->3d降噪
cmd25 = ["cat /usr/config/ipccfg.conf|awk -F 3DNoiseReduceLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##26.读取配置文件--->动态调节
cmd26 = ["cat /usr/config/ipccfg.conf|awk -F BacklightMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##27.读取配置文件--->背光补偿灵敏度
cmd27 = ["cat /usr/config/ipccfg.conf|awk -F BacklightLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##28.读取配置文件--->强光抑制灵敏度
cmd28 = ["cat /usr/config/ipccfg.conf|awk -F SLCLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##29.读取配置文件--->宽动态灵敏度
cmd29 = ["cat /usr/config/ipccfg.conf|awk -F WDRLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##30.读取配置文件--->图像增强
cmd30 = ["cat /usr/config/ipccfg.conf|awk -F ImageEnhance '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##31.读取配置文件--->透雾灵敏度
cmd31 = ["cat /usr/config/ipccfg.conf|awk -F DefogLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##32.读取配置文件--->畸变校正
cmd32 = ["cat /usr/config/ipccfg.conf|awk -F IspExpAllAutoMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]

    ##33.读取配置文件--->防抖
cmd33 = ["cat /usr/config/ipccfg.conf|awk -F ImageEnhance '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]  
    ##34.读取配置文件--->防抖等级
cmd34 = ["cat /usr/config/ipccfg.conf|awk -F StablizerLevel '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]

    ##35.读取配置文件--->翻转模式
cmd35 = ["cat /usr/config/ipccfg.conf|awk -F RotateFlipMode '{print $3}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]

    ##36.读取配置文件---> 帧率
cmd36 = ["cat /usr/config/ipccfg.conf|awk -F FrameRate '{print $2}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##37.读取配置文件--->分辨率VidWide
cmd37 = ["cat /usr/config/ipccfg.conf|awk -F VidWide '{print $2}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##38.读取配置文件--->分辨率VidHeight
cmd38 = ["cat /usr/config/ipccfg.conf|awk -F VidHeight '{print $5}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##39.读取配置文件--->码率
cmd39 = ["cat /usr/config/ipccfg.conf|awk -F BitRate '{print $2}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##40.读取配置文件--->I帧间隔
cmd40 = ["cat /usr/config/ipccfg.conf|awk -F MaxKeyRate '{print $2}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##41.读取配置文件--->RcMode码率类型
cmd41 = ["cat /usr/config/ipccfg.conf|awk -F RcMode '{print $2}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##42.读取配置文件--->EncType编码格式
cmd42 = ["cat /usr/config/ipccfg.conf|awk -F EncType '{print $5}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##43.读取配置文件--->EncQuality 图像质量
cmd43 = ["cat /usr/config/ipccfg.conf|awk -F EncQuality '{print $2}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##44.读取配置文件--->H264ProfiledId编码复杂度
cmd44 = ["cat /usr/config/ipccfg.conf|awk -F H264ProfiledId '{print $2}'|awk -F , '{print $1}'|awk -F : '{print $2}'"]
    ##45.读取配置文件--->编码裁剪启用
cmd45 = ["cat /usr/config/ipccfg.conf|awk -F Crop '{print $2}'|awk -F Enable '{print $2}'|awk -F ':' '{print $2}'|awk -F "," '{print $1}'"]



#  cat /usr/config/ipccfg.conf|awk -F SSHEnable '{print $2}'|awk -F , '{print $1"" }'|awk -F : '{print $2}'  ##ssh是否开启