# -*- coding: utf-8 -*-  
from distutils.core import setup  
import py2exe

includes = ["encodings", "encodings.*","api","runtest"]    ##逗号分开模块列表
options = {"py2exe":    
            {"compressed": 1,  #压缩    
             "optimize": 2,    
             "ascii": 1,    
             "includes":includes,    
             #"bundle_files": 2   #是所有文件打包成一个exe文件 
            }}  
setup(  
    options=options,    
    #zipfile=None,  ##配合options和bundle_files使用，None把所有东西打包进.exe文件中
    #console=[{"script": "GUIwwb.py", "icon_resources": [(1, "ooopic_1483782995.ico")]}],
    windows=[{"script": "KIPCAutoTest.py","icon_resources": [(1, "user.ico")]}],  
    data_files=[(".",["Config.ini","IPC_v7_message.xlsx","ipc.ico"])],   ##指定额外的配置文件，那么py2exe能将这些文件拷贝到dist子目录中     
    version = "v1.1.20170107",   
    description = "KDwebAutoTest V1.1.0",   
    name = "KDwebAutoTest（V1.1）",   
)  

    
    
