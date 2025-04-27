# 檔案操作流程:1.開啟檔案 2.讀取或寫入 3.關閉檔案
# 第一步開啟檔案:
# 開啟檔案基本語法:
# 檔案物件=open(檔案路徑,mode=開啟模式)
# 開啟模式有三種:讀取模式:r,寫入模式:w,讀寫模式:r+

# 第二步讀取或寫入:
# 讀取全部文字語法:
# 檔案名稱.read()

# 第三步關閉檔案:
# 基本語法:檔案物件.close()


# 範例一:如何開啟中文檔案，並關閉檔案
# 開啟後會在專案資料夾裡產生一個檔案
# 如果想打中文，沒有多打這一行 encoding="utf-8"，會出現下列錯誤資訊:
# UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-2: character maps to <undefined>
file=open("data.txt",mode="w",encoding="utf-8")
file.write("Hello File\nSecond line")
file.write("好棒棒")
file.close()

# 範例二:最佳實務
# with open(檔案路徑,mode=開啟模式) as 檔案物件:
# 以上區塊會自動安全的關閉檔案
with open("data1.txt",mode="w",encoding="utf-8") as file1:
     file1.write("測試中文")
with open("data1.txt", mode="r", encoding="utf-8") as file1:
          data=file1.read()
print(data)

# 範例三:把檔案中的的數字資料，一行一行的讀取出來，並計算總合
# 如果要一次讀取一行，可以用 for 迴圈:
# for 變數 in 檔案物件:
# 從檔案依序讀取每行文字到變數中
with open("data2.txt",mode="w") as file2:
     file2.write("5\n3")
sum=0
with open("data2.txt",mode="r") as file2:
     for line in file2:
          sum+=int(line)
print(sum)

# 範例四: 如何讀取json檔案，並列印json檔案字典裡的資料
# 讀取JSON格式:
# import json
# 讀取到的資料=json.load(檔案物件)
# 寫入JSON格式:
# import json
# json.dump(要寫入的資料,檔案物件)
import json
with open ("config.json",mode="r") as file3:
    data=json.load(file3) #data是一個字典資料
print("name:",data["name"])
print("version:",data["version"])

# 範例五: (承上)如何修改json檔案內的資料: 1.先修改2.再複寫
# 從檔案中讀取 json 資料，放入變數 data 裡面
data["name"]="New Name1"  #修改變數中資料
with open("config.json","w") as file4:
    json.dump(data,file4) #最後，把最新的資料複寫回檔案中