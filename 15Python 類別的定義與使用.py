# 類別的定義與使用
# 類別:封裝變數或函式     封裝的變數或函式，統稱類別的屬性
# 定義類別 -> 使用類別    要先定義(建立)類別，然後才能使用類別中封裝的屬性

# 基本語法
#class 類別名稱:   (跟變數一樣第一個字不可以是數字，通常習慣第一個字大寫)
    #定義封裝的變數
    #定義封裝的函式

# 程式範例

# 定義 Test 類別
#class Test:
    #x=3 #定義變數
    #def say(): # 定義函式
        #print("Hello")

# 基本語法 
# 類別名稱.屬性名稱

# 程式範例
# 定義 Test 類別
#class Test:
#   x=3
#   def say():
#       print("Hello")

# 使用 Test 類別 
# Test.x+3   # 取得屬性 x 的資料 3    然後 +3
# Test.say() # 呼叫屬性 say 函式    

#------------------------

# 定義類別、與類別屬性 (封裝在類別中的變數和函式)
# 定義一個類別 IO, 有兩個屬性 supportedSrcs 和 read 
class IO:  # IO input 跟 output 的簡稱 一個變數
    supportedSrcs=["console","file"]    # 設定變數 支援的資料來源  可以有 終端機 檔案
    def read (src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Read from", src)

# 使用類別   類別的名稱.屬性的名稱
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")