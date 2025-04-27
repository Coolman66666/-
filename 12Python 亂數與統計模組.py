# 亂數、統計模組
# 內建模組 : random , statistics   做數據分析很重要的基礎

# 亂數模組
# 載入模組
#import random

# 隨機選取
import random

# 從列表中隨機選取 1 個資料    ( 1個用 choice )
random.choice([0,1,5,8])

# 從列表中隨機選取 2 個資料    ( 2個以上用 sample 不能超過列表的長度 )
random.sample([0,1,5,8],2)

# 隨機調換順序
import random

# 將列表的資料(就地)隨機調換順序   會對列表本身的資料進行修改、調換
data=[0,1,5,8]
random.shuffle(data)
print(data)

# 隨機亂數
import random

# 取得 0.0 ~ 1.0 之間的隨機亂數
random.random()     # 取 0 ~ 1 之間的隨機亂數
random.uniform(0.0,1.0)   # 區間內的隨機亂數   機率相同

# 常態分配亂數
import random

# 取得平均數 100 標準差 10 的
# 常態分配亂數
random.normalvariate(100,10)    # 前面是平均數 後面是標準差
# 這樣取到的數 
# 大部分取到的數都在一個標準差內 90 ~ 110 (68%) 
# 更大部分是兩個標準差內 80 ~ 120 (95%) 
# 極大部分是三個個標準差內 70 ~ 130 (99.7%)

# 載入統計模組
#import statistics

# 計算平均數
import statistics

# 計算列表中數字的平均數
statistics.mean([1,4,6,9])

# 計算列表中數字的中位數
statistics.median([1,4,6,9])

# 計算列表中數字的標準差
statistics.stdev([1,4,6,9])

#--------------

# 隨機模組
import random

# 隨機選取
data=random.choice([1,5,6,10,20])
print(data)

# 複數的隨機選取  會回傳一個列表資料出來
data=random.sample([1,5,6,10,20],3)
print(data)

# 隨機調換順序 (就是洗牌的概念)
data=[1,5,8,20]
random.shuffle(data)
print(data)

# 隨機取得亂數 
data=random.random()  # 0 ~ 1 之間的隨機亂數
print(data)

data=random.uniform(60,100) # 60 ~ 100 之間的隨機亂數
print(data)

# 取得常態分配亂數
# 平均數 100, 標準差 10, 得到的資料多數在 90~ 110 之間
data=random.normalvariate(100,10)      
print(data)

# 平均數 0, 標準差 5, 得到的資料多數在 -5 ~ 5 之間
data=random.normalvariate(0,5)
print(data)


# 統計模組
import statistics as stat # 用別名來稱呼這個模組  操作起來會比較方便
data=stat.mean([1,4,5,8])
print(data)

data=stat.median([1,2,3,4,5,8,100])   # 用中位數   比較符合大部分人的情況   因為極端值不會進來
print(data)

data=stat.median([1,2,3,4,6,5,8,100])
print(data)

data=stat.stdev([1,2,3,4,5,8,10])  # 標準差   資料的散布狀況
print(data)

# 平均數、中位數、標準差、常態分配

