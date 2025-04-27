#Point 實體物件的設計:平面座標上的點
class Point: 
    def __init__(self):
     self.x=3
     self.y=4
#建立第一個實體物件
p1=Point()
print(p1.x,p1.y)
#建立第二個實體物件
p2=Point()
print(p2.x,p2.y)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p1=Point(7,8)
print(p1.x,p1.y)
p2=Point(5,6)
print(p2.x,p2.y)


#Fullname 實體物件的設計:分開紀錄姓、名資料的全名
class Fullname:
    def __init__(self):
        self.first="C.W"
        self.last="Peng"
name1=Fullname()
print(name1.first,name1.last)


class Fullname:
  def __init__(self,first,last):
      self.first=first
      self.last=last
name1=Fullname("Q.A","Chou")
print(name1.first,name1.last)
name2=Fullname("T.Y","Lin")
print(name2.first,name2.last)