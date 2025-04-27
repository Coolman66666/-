# 封包(package)的使用
# 封包:包含模組的資料夾   用來整理、分類模組程式    
# 建立封包
# 專案檔案配置
#-專案資料夾
    #-主程式.py
    #封包資料夾
        #-__init__.py  (有建立這個程式，這個資料夾就會被當成封包來看待 兩個底線init兩個底線.py)
        #-模組一.py
        #-模組二.py

# 專案檔案配置範例
#-專案資料夾
    #-main.py
    #-geometry
        #-__init__.py
        #-point.py
        #-line.py

# 基本語法
#import 封包名稱.模組名稱
#import 封包名稱.模組名稱 as 模組別名

# 主程式
import geometry.point
result=geometry.point.distance(3,4)
print(result)

import geometry.point as x0
result=x0.distance(3,4)
print("距離: ",result)

import geometry.line
result=geometry.line.slope(1,1,3,3)
print("斜率: ",result)

import geometry.line as line
result=line.slope(1,1,3,3)
print("斜率: ",result)

