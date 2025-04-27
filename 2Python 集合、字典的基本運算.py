s1 = {3,4,5}
s2 = {4,5,6,7}
s3 = s1&s2  # 交集 ：取兩個集合中, 相同的資料
s4 = s1|s2  # 聯集 : 取兩個集合中的所有資料,但不重複取
s5 = s1 - s2 #差集： 從S1中, 減去和s2 重疊的部分
s6 = s1^s2 # 反交集： 取兩個集合中, 不重疊的部分
print(3 in s1)      #True
print(10 not in s1) #True
print(s3)
print(s4)
print(s5)
print(s6)

s = set("Hello") # 把字串中的字母拆解成集合：set(字串)
print(s)
print("H" in s)
print("A" in s)
print("H" in s)

#字典的運算: key-value 配對
dic = {"apple":"蘋果", "bug":"蟲蟲"}
dic["apple"]= "小蘋果"
print(dic["apple"])
print("apple" in dic) #判斷 key 是否存在
print("test" not in dic) 
print(dic)
del dic["apple"] #刪除字典中的鍵值對 (key-value pair)
print(dic)
dic = {x:x*2 for x in [3, 4, 5]}#從列表的資料產生字典 ## xxx可代換, for in 是固定的, 列表要給他一個列表
print(dic)