# 實體物件的建立與使用-下篇

# 類別的兩種用法
# 1.類別與類別屬性
# 2.類別與實體物件、實體屬性、實體方法

# 實體屬性 : 封裝在實體物件中的變數
# 程式範例
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
# 建立實體物件，並取得實體屬性資料
p=Point(1,5)
print(p.x+p.y)

# 實體方法 : 封裝在實體物件中的函式
# 基本語法
#class 類別名稱:
#   定義初始化函式
#   def __init__(self):
#       定義實體屬性
#   定義實體方法/函式
# 建立實體物件，放入變數obj中
#obj=類別名稱()

# 寫更細一點
# 基本語法
#class 類別名稱:
#   定義初始化函式
#   def __init__(self):
#       封裝在實體物件中的變數
#   def 方法名稱(self,更多自訂參數):
#       方法主體，透過 self 操作實體物件
# 建立實體物件，放入變數obj中
#obj=類別名稱()

# 基本語法
# 實體物件.實體方法名稱(參數資料)

# 程式範例
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)

p=Point(1,5) # 建立實體物件
p.show()     # 呼叫實體方法

#----------------------------

# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # 定義實體方法(特色是self一定要寫)   (其實就是封裝在類別內的函式)
    def show(self):
        print(self.x,self.y)
    def distance(self,targetX,targetY):
        return(((self.x-targetX)**2+(self.y-targetY)**2)**(1/2))
p=Point(3,4)
p.show() # 呼叫實體方法 / 函式
answer=p.distance(0,0)
print(answer)  # 記標座標 3,4 和座標 0,0 之間的距離


# File 實體物件的設計: 包裝檔案讀取的程式

class File:
    # 初始化函式   建立實體物件
    def __init__(self,name):
        self.name=name
        self.file=None # 尚未開啟檔案: 初期是 None
    # 實體方法
    def open(self):   # 這是我們建立的開啟檔案的方法
        self.file=open(self.name,mode="r",encoding="utf-8")  # 這是 python 內建的開啟檔案的函式
    def read(self):
        return self.file.read()

# 讀取第一個檔案
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)

# 讀取第二個檔案
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)