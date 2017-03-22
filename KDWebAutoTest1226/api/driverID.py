#coding:utf-8
#!/usr/bin/env python
##################################################################
#IPC客户端所有对象ID
#对象对位器
#2016-05-3修改
##################################################################
from selenium.webdriver.common.by import By

class WebID():      ##页面基本操作，元素定位等
    "IPCV7所有对象ID"
    #############以对象ID为定位点的定位器################################
    #find_element(By.ID,"username")
    #find_element(By.NAME,"logininput")
    #find_element(By.CLASS_NAME,"logininputblur inputbackground")
    #find_element(By.XPATH,".//*[@id='username']")
    ######登陆界面对象ID################################################
    username_loc=(By.ID,"username")    ##用户名
    #username_loc=(By.NAME,"logininput")    ##用户名
    password_loc=(By.ID,"password")    ##密码
    login_loc=(By.ID,"b_Login")     ##登陆按钮
    #"主页面"定位器
    MenuViewer_loc=(By.ID,"MenuViewer")     ##实时浏览
    MenuPlayback_loc=(By.ID ,"MenuPlayback")    ##录像回放
    MenuPic_loc=(By.ID,"MenuPic")   ##图片管理
    MenuConfig_loc=(By.ID,"MenuConfig")     ##配置
    
    #1. 主页面“实时浏览”对象定位器
    changePlay_loc=(By.ID,"changePlay")   ##主辅流切换
    ptz_right_loc=(By.ID,'ptz_right')    ##PTZ控制右
    capture_loc=(By.ID,'capture')    ##抓拍
    #2. 主页面“录像回放”对象定位器
    
    #3. 主页面“图片管理”对象定位器
    
    
    #4. 主页面“配置”      对象定位器
    aMLocalConfig_loc=(By.ID,"aMLocalConfig")   ##本地配置
    Mfastset_loc=(By.ID,"Mfastset")     ##快速配置
    aNetwork_loc=(By.ID,"aNetwork")     ##网络
    aVideoCamera_loc=(By.ID,"aVideoCamera")     ##摄像机
    aEvent_loc=(By.ID,"aEvent")      ##事件
    aStorage_loc=(By.ID,"aStorage") ##存储
    aBaseConfig_loc=(By.ID,"aBaseConfig")      ##系统
    
    #4.1    一级菜单“本地配置”菜单下定位器
    #4.1.1    二级菜单“本地配置”下对象定位器
    MLocalConfig_loc=(By.ID,"MLocalConfig")     ##本地配置
    tePreviewPicPath_loc=(By.ID,"tePreviewPicPath")     ##抓拍---浏览抓拍保存路径
    #4.2    一级菜单“ 快速配置”菜单下定位器####
    
    #4.3    一级菜单“网络”菜单下定位器####
    
    #4.4     一级菜单“摄像机”菜单下定位器
    aImagsSettings_loc=(By.ID,"aImagsSettings") ##图像
    aOSD_loc=(By.ID,"aOSD") ##OSD
    aVideo_loc=(By.ID,"aVideo") ##视频
    aAudio_loc=(By.ID,"aAudio") ##音频
    
    #4.4.1     二级菜单“ 图像---图像效果”菜单下对象
    divImagsSets_loc=(By.ID,"divImagsSets")   ##图像效果
    lightnessh5_loc=(By.ID,"lightnessh5")   ##图像调节
    lightness_value_loc=(By.ID,"lightness_value")   ##图像亮度
    contrast_value_loc=(By.ID,"contrast_value")   ##图像对比度
    saturation_value_loc=(By.ID,"saturation_value")   ##图像饱和度
    sharpness_value_loc=(By.ID,"sharpness_value")   ##图像锐度
    
    exposureh5_loc=(By.ID,"exposureh5")     ##曝光
    GainMode_loc=(By.ID,"GainMode")     ##增益 auto，manual
    gainmax_value_loc=(By.ID,"gainmax_value")   ##增益上限0~100
    gainlevel_value_loc=(By.ID,"gainlevel_value")
    IrisType_loc=(By.ID,"IrisType")     ##光圈模式dc_irisauto DC-IRIS自动，dc_irismanual DC-IRIS手动，p_irismanual P-IRIS手动
    irislevel_value_loc=(By.ID,"irislevel_value")   ##光圈灵敏值 1~100
    irissize_value_loc=(By.ID,"irissize_value")    ##光圈大小
    ShuterMode_loc=(By.ID,"ShuterMode")     ##快门模式：快门值auto 自动，manual 手动
    Shutermin_loc=(By.ID,"Shutermin")   
    ##快门下限：1/1，1/2,1/7.5，1/10,1/15,1/25,1/50
    Shutterlevel_loc=(By.ID,"Shutterlevel")     ##快门等级
    AntiFlickerMode_loc=(By.ID,"AntiFlickerMode")   ##防闪烁 50hz，60hz，auto 自然光
    
    whiteblanceh5_loc=(By.ID,"whiteblanceh5")   ##白平衡按钮
    WhiteBalance_loc=(By.ID,"WhiteBalance")    ##白平衡下拉框
    ##白平衡选择框  manual 手动白平衡，auto1 自动白平衡1，auto2 自动白平衡2，lock 锁定白平衡，fluorescentlight 日光灯，filamentlight 白炽灯，warmlight 暖光灯，natural 自然光
    R_value_loc=(By.ID,"R_value")   ##手动白平衡 R值
    B_value_loc=(By.ID,"B_value")   ##手动白平衡 B值
    
    ircutfilterh5_loc=(By.ID,'ircutfilterh5')   ##日夜转换
    IrcutfilterType_loc=(By.ID,'IrcutfilterType')    ##日夜转换下拉框
    daytonightlevel_value_loc=(By.ID,'daytonightlevel_value')   ##自动（增益触发）灵敏度
    daytonight_value_loc=(By.ID,'daytonight_value')     ##自动（增益触发）日夜转换等待时间5~120
    threshold_value_loc=(By.ID,'threshold_value')   ##自动（增益触发）日夜转换阈值
    
    ImageEnhancementh5_loc=(By.ID,'ImageEnhancementh5')     ##图像增强
    mode2d_loc=(By.ID,'mode2d')     ##2D降噪模式
    D2_value_loc =(By.ID,'2D_value')     ##2D降噪
    mode3d_loc=(By.ID,'mode3d')     ##3D降噪模式
    D3_value_loc=(By.ID,'3D_value')     ##3D降噪
    backlightmode_loc=(By.ID,'backlightmode')     ##动态调节
    imageenhance_slect_loc=(By.ID,'imageenhance_slect')     ##图像增强
    selectassistmalf_loc=(By.ID,'selectassistmalf')     ##畸变校正
    
    Antishake5_loc=(By.ID,'Antishake5')     ##防抖
    ModeAntishake_loc=(By.ID,'ModeAntishake')     ##防抖模式
    antishake_value_loc=(By.ID,'antishake_value')     ##防抖等级
    
    otherh5_loc=(By.ID,'otherh5')   ##翻转与回显
    selectRotateMode_loc=(By.ID,'selectRotateMode')   ##翻转模式
    corridormode_loc=(By.ID,'corridormode')   ##手动--走廊模式
    imagemode_loc=(By.ID,'imagemode')   ##手动--镜像模式
    cvbsmode_loc=(By.ID,'cvbsmode')   ##本地回显
    
    #4.4.2     二级菜单“OSD”菜单下对象
    
    #4.4.3     二级菜单“视频”菜单下对象
    MVideo_loc=(By.ID,'MVideo')   ##视频编码
    Mcropping_loc=(By.ID,'Mcropping')   ##编码裁剪
    mROI_loc=(By.ID,'mROI')   ##ROI
    Mprivacymasks_loc=(By.ID,'Mprivacymasks')   ##视频遮挡
    Moverlay_loc=(By.ID,'Moverlay')   ##视频信息叠加
    #4.4.3.1   “视频---视频编码”菜单下对象
    multivideoType_loc=(By.ID,'multivideoType')   ##多码流
    StreamTypeIn_loc=(By.ID,'StreamTypeIn')   ##主辅码流
    videoResolution_loc=(By.ID,'videoResolution')   ##分辨率
    videoQualityControlType_loc=(By.ID,'videoQualityControlType')   ##码率类型
    fixedQuality_loc=(By.ID,'fixedQuality')   ##图像质量
    maxFrameRate_loc=(By.ID,'maxFrameRate')   ##视频帧率
    constantBitRate_loc=(By.ID,'constantBitRate')   ##编码上限
    videoCodecType_loc=(By.ID,'videoCodecType')   ##编码格式
    selectCodecComplexity_loc=(By.ID,'selectCodecComplexity')   ##编码复杂度
    IntervalFrameI_loc=(By.ID,'IntervalFrameI')   ##I帧间隔
    constantBitRate_loc=(By.ID,"constantBitRate")   ##码率上限
    ConfigBtn_loc=(By.ID,"ConfigBtn")     ##视频编码页面“保存”按钮
    #4.4.3.2   “视频---编码裁剪”菜单下对象
    checkobjcropping_loc=(By.ID,"checkobjcropping")  ##启用选择框
    Selectedcropping_loc=(By.ID,"Selectedcropping")  ##开始绘制
    ClearAllcropping_loc=(By.ID,"ClearAllcropping")  ##清除绘制
    SaveConfigBtn_loc=(By.ID,"SaveConfigBtn")  ##保存按钮
    #4.4.3.3   “视频---ROI”菜单下对象
    checkobjroi_loc=(By.ID,"checkobjroi")  ##启用选择框
    SelectedRoi_loc=(By.ID,"checkobjroi")  ##选择区域
    ClearAllRoi_loc=(By.ID,"ClearAllRoi")  ##清除区域
    codelevel_loc=(By.ID,"codelevel")  ##等级
    #SaveConfigBtn_loc=(By.ID,"SaveConfigBtn")  ##选择区域
    #4.4.3.4   “视频---视频遮挡”菜单下对象
    checkprivacymasks_loc=(By.ID,"checkprivacymasks")  ##启用选择框
    shieldstr_loc=(By.ID,"shieldstr")  ##开始绘制
    shieldclear_loc=(By.ID,"shieldclear")  ##清除绘制
    shieldcolortype_loc=(By.ID,"shieldcolortype")  ##遮蔽颜色
    #SaveConfigBtn_loc=(By.ID,"SaveConfigBtn")  ##保存按钮
    #“4.4.3.5   视频---视频信息叠加”菜单下对象
    checkGPS_loc=(By.ID,"checkGPS")  ##GPS信息
    checkPosition_loc=(By.ID,"checkPosition")  ##镜头方位新
    checkSimpleitl_loc=(By.ID,"checkSimpleitl")  ##基础智能信息
    checkDigimarc_loc=(By.ID,"checkDigimarc")  ##数字水印
    input_save_loc=(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/div[5]/span/input")  ##保存按钮
    #“4.4.4.1   视频---音频编码”菜单下对象
    MAudiocode_loc=(By.ID,"MAudiocode")  ##音频编码
    audioSoureType_loc=(By.ID,"audioSoureType")  ##音频源类型
    audioSourechn_loc=(By.ID,"audioSourechn")  ##编码通道
    AudiosamprateType_loc=(By.ID,"AudiosamprateType")  ##采样率
    encVol_value_loc=(By.ID,"encVol_value")  ##编码音量
    AudioEncType_loc=(By.ID,"AudioEncType")  ##编码格式
    videoBindType_loc=(By.ID,"videoBindType")  ##视频编码通道
    videoBindId1_loc=(By.ID,"videoBindId1")  ##绑定通道---音频编码通道1
    videoBindId2_loc=(By.ID,"videoBindId2")  ##绑定通道---音频编码通道2
    SaveAudiocode_loc=(By.ID,"SaveAudiocode")  ##保存按钮
    #“4.4.4.1   视频---音频解码”菜单下对象
    MAudiodecoder_loc=(By.ID,"MAudiodecoder")  ##音频解码
    decVol_value_loc=(By.ID,"decVol_value")  ##解码音量
    mixerrec_loc=(By.ID,"mixerrec") ##混音录像
    SaveConfigAudiodecoder_loc=(By.ID,"SaveConfigAudiodecoder") ##保存按钮
    #4.5    一级菜单“事件”菜单下定位器
    
    #4.6    一级菜单“存储”菜单下定位器
      
    #4.7    一级菜单 "系统"下对象
    aDeviceInformation_loc=(By.ID,"aDeviceInformation")     ##设备信息
    aSecurity_loc=(By.ID,"aSecurity")   ##用户安全
    aDateTime_loc=(By.ID,"aDateTime")   ##时间设置
    aSerialPost_loc=(By.ID,"aSerialPost")   ##串口
    aLog_loc=(By.ID,"aLog")     ##日志管理
    aSystemMaintenance_loc=(By.ID,"aSystemMaintenance")     ##系统维护
    
    #4.7. 1    二级菜单“设备信息”下对象定位器
    
    #4.7. 2    二级菜单“用户安全”下对象定位器
    MSafetyService_loc = (By.ID,"MSafetyService") 
    IsEnableSSH_loc = (By.ID,"IsEnableSSH") 
    SaveSafetyService_loc = (By.ID,"SaveSafetyService") 
    #4.7. 3    二级菜单“时间设置”下对象定位器
    
    #4.7. 4   二级菜单“串口”下对象定位器
    
    #4.7. 5    二级菜单“日志管理”下对象定位器
    
    #4.7. 6    二级菜单“系统维护”下对象定位器
    aReboot_loc =(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/span[2]/input")
    aSimpleRestore_loc =(By.XPATH,"html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[9]/span[2]/input")

    





