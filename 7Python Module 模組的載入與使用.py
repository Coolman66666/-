#載入內建的 sys 模組並取得資訊
import sys as s
print(s.platform)
print(s.maxsize)

#建立geometry模組,載入使用(python的模組就是程式檔案)
import geometry
result=geometry.distance(1,1,5,5)
print(result)

#調整搜尋模組的路徑
import sys
print(sys.path)#印出模組搜尋路徑(當要載入模組時，python會按照路徑搜尋模組，所以模組必須在這些路徑之中才有機會找到)
import geometry
print(geometry.distance(1,1,5,5))#if 將檔案移離路徑會找不到

#因為檔案不在路徑中所以我們要調整搜尋模組路徑
import sys
sys.path.append("modules")#在模組的搜尋路徑列表中"新增路徑"
print(sys.path)
import geometry
print(geometry.distance(1,1,5,5))